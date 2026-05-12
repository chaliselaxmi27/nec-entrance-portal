import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from admission.models import Notice, Scholarship
from programs.models import Program
from core.models import SiteSetting
from pages.models import Download


def normalize_text(text: str) -> str:
    return (text or "").strip().lower()


def find_program_from_message(message: str):
    programs = Program.objects.filter(is_active=True)

    for program in programs:
        name = normalize_text(program.name)
        if name and name in message:
            return program

    for program in programs:
        words = normalize_text(program.name).replace("(", " ").replace(")", " ").replace("-", " ").split()
        matched_words = [word for word in words if len(word) > 2 and word in message]
        if matched_words:
            return program

    return None


def get_latest_notice_reply():
    latest_notice = Notice.objects.order_by("-published_date", "-id").first()
    if latest_notice:
        return f"Latest notice: {latest_notice.title}"
    return "Please check the Notices section for the latest updates."


def get_program_list_reply():
    programs = Program.objects.filter(is_active=True).order_by("display_order", "name")[:8]
    if programs.exists():
        names = ", ".join(program.name for program in programs)
        return f"Available programs include: {names}."
    return "Program information is available in the Offered Programs section."


def get_program_detail_reply(program):
    parts = [program.name]

    if getattr(program, "seats", None):
        parts.append(f"Seats: {program.seats}")

    if getattr(program, "shift", None):
        parts.append(f"Shift: {program.shift}")

    if getattr(program, "duration", None):
        parts.append(f"Duration: {program.duration}")

    if getattr(program, "short_description", None):
        parts.append(str(program.short_description))

    return " | ".join(parts)


def get_download_reply(message: str):
    downloads = Download.objects.filter(is_active=True).order_by("order", "-created_at")

    for item in downloads:
        title = normalize_text(getattr(item, "title", ""))
        if title and title in message:
            return f"You can find this in Downloads/Other Links: {item.title}"

    if "fee" in message:
        fee_file = downloads.filter(title__icontains="fee").first()
        if fee_file:
            return f"Fee information is available in Downloads/Other Links: {fee_file.title}"
        return "Fee structure is available in the Downloads/Other Links section."

    if "syllabus" in message:
        syllabus_file = downloads.filter(title__icontains="syllabus").first()
        if syllabus_file:
            return f"Syllabus is available in Downloads/Other Links: {syllabus_file.title}"
        return "Syllabus is available in the Downloads/Other Links section."

    if "prospectus" in message:
        prospectus = downloads.filter(title__icontains="prospectus").first()
        if prospectus:
            return f"Prospectus is available in Downloads/Other Links: {prospectus.title}"
        return "Please check the Downloads/Other Links section for the prospectus."

    if "model question" in message or "question" in message:
        question_file = downloads.filter(title__icontains="question").first()
        if question_file:
            return f"Model questions are available in Downloads/Other Links: {question_file.title}"
        return "Please check the Downloads/Other Links section for model questions."

    return None


def generate_chat_reply(message: str) -> str:
    message = normalize_text(message)
    site = SiteSetting.objects.first()

    if not message:
        return "Please type your question."

    if any(word in message for word in ["hi", "hello", "hey", "namaste"]):
        return "Hello! Welcome to NEC Admission Assistant. You can ask about admission, fee, syllabus, scholarship, notices, programs, or contact."

    if any(word in message for word in ["thanks", "thank you"]):
        return "You're welcome. Feel free to ask anything about NEC admission, notices, programs, or downloads."

    if any(word in message for word in ["admission", "apply", "application", "form"]):
        return "For admission, please check the latest admission notices and complete the required application process. You can also ask me about fee, syllabus, scholarship, or programs."
    if any(word in message for word in ["entrance", "apply now", "enquiry" ]):
        return "For Entrance, please fill the enqiry form and complete the required application process."
    if "notice" in message or "notices" in message or "latest notice" in message:
        return get_latest_notice_reply()

    if "scholarship" in message:
        scholarship = Scholarship.objects.first()
        if scholarship:
            return f"Scholarship information: {scholarship.title}"
        return "Scholarship information is available in the scholarship section of the website."
        

    if any(word in message for word in ["contact", "phone", "email", "call"]):
        phone = getattr(site, "phone", None) if site else None
        email = getattr(site, "email", None) if site else None

        if phone and email:
            return f"You can contact NEC at {phone} or {email}."
        if phone:
            return f"You can contact NEC at {phone}."
        if email:
            return f"You can contact NEC at {email}."

        return "Please check the Contact section or footer for phone number and email."

    download_reply = get_download_reply(message)
    if download_reply:
        return download_reply

    if any(word in message for word in ["program", "programs", "course", "courses", "faculty"]):
        return get_program_list_reply()

    program = find_program_from_message(message)
    if program:
        return get_program_detail_reply(program)

    return "Sorry, I could not understand that clearly. Please ask about admission, fee, syllabus, scholarship, notices, programs, downloads, or contact."


@csrf_exempt
def chat_api(request):
    if request.method != "POST":
        return JsonResponse({"reply": "Invalid request method. Use POST."}, status=400)

    try:
        data = json.loads(request.body.decode("utf-8"))
        message = data.get("message", "")
        reply = generate_chat_reply(message)
        return JsonResponse({"reply": reply})
    except Exception as e:
        print("CHATBOT ERROR:", e)
        return JsonResponse({"reply": "Sorry, something went wrong while processing your request."}, status=500)