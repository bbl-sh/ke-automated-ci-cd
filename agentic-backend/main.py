from fastapi import FastAPI
from fastapi.responses import HTMLResponse, StreamingResponse
import io
from xhtml2pdf import pisa
import markdown
from test import run_langgraph
from generate_html import generate_html_content

app = FastAPI()


@app.get("/report", response_class=HTMLResponse)
async def display_report():
    final_state = run_langgraph()
    html_content = generate_html_content(final_state)
    return html_content

@app.get("/download")
async def download_report():
    final_state = run_langgraph()
    html_content = generate_html_content(final_state)
    pdf_buffer = io.BytesIO()
    pisa.CreatePDF(html_content, dest=pdf_buffer)
    pdf_buffer.seek(0)
    return StreamingResponse(
        pdf_buffer,
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=ai_suggestions_report.pdf"}
    )
