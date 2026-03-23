from django.shortcuts import render
from django.http import FileResponse
import mammoth
from weasyprint import HTML


def upload_file(request):

    if request.method == "POST":

        file = request.FILES.get("document")

        with open("input.docx", "wb+") as f:
            for chunk in file.chunks():
                f.write(chunk)

        # Convert DOCX → HTML
        with open("input.docx", "rb") as docx_file:
            result = mammoth.convert_to_html(docx_file)
            html = result.value

        # Convert HTML → PDF
        HTML(string=html).write_pdf("output.pdf")

        return FileResponse(open("output.pdf", "rb"), as_attachment=True)

    return render(request, "upload.html")