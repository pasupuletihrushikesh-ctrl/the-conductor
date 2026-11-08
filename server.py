from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import uvicorn

app = FastAPI(
    title="The Conductor — Multi-Agent Orchestrator API",
    version="1.0.0",
    description="Central Orchestrator master routing engine emitting Maroon & Beige UI command blocks."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ProjectRequest(BaseModel):
    user_prompt: str
    current_agent: Optional[str] = "Orchestrator"

class UICommandBlock(BaseModel):
    ui_action: str = "AGENT_TRANSITION"
    theme_accent: str = "maroon"
    background: str = "beige"
    transition_style: str = "smooth_slide"
    from_agent: str
    to_agent: str
    status_message: str

class OrchestrationResponse(BaseModel):
    ui_command: UICommandBlock
    orchestrator_update: str
    active_agent: str
    agent_output: str

AGENT_ROSTER = {
    "Architect Agent": {
        "role": "System design, project planning, and structural logic",
        "keywords": ["architecture", "plan", "structure", "system", "blueprint", "database", "scale"]
    },
    "Visual Agent": {
        "role": "UI/UX design, visual asset generation, and aesthetic formatting",
        "keywords": ["design", "ui", "ux", "landing page", "color", "layout", "visual", "art", "theme"]
    },
    "Creator Agent": {
        "role": "Copywriting, content generation, and creative brainstorming",
        "keywords": ["copy", "content", "write", "marketing", "story", "poem", "headline", "slogan"]
    },
    "Logic Agent": {
        "role": "Coding, debugging, data analysis, and mathematical problem-solving",
        "keywords": ["code", "script", "function", "api", "bug", "sql", "math", "algorithm", "python"]
    },
    "Reviewer Agent": {
        "role": "Quality assurance, proofreading, and final project polishing",
        "keywords": ["review", "test", "audit", "qa", "verify", "check", "polish", "validate"]
    }
}

@app.post("/api/route", response_model=OrchestrationResponse)
async def route_project(request: ProjectRequest):
    prompt_lower = request.user_prompt.lower()
    from_agent = request.current_agent or "Orchestrator"

    # Evaluate best specialized agent
    to_agent = "Architect Agent"
    if any(k in prompt_lower for k in AGENT_ROSTER["Visual Agent"]["keywords"]):
        to_agent = "Visual Agent"
    elif any(k in prompt_lower for k in AGENT_ROSTER["Logic Agent"]["keywords"]):
        to_agent = "Logic Agent"
    elif any(k in prompt_lower for k in AGENT_ROSTER["Creator Agent"]["keywords"]):
        to_agent = "Creator Agent"
    elif any(k in prompt_lower for k in AGENT_ROSTER["Reviewer Agent"]["keywords"]):
        to_agent = "Reviewer Agent"

    # Status message & Orchestrator rationale
    if to_agent == "Visual Agent":
        status = "Designing layout and aesthetic presentation in Maroon & Beige..."
        update = f"I have received your request. I am handing this over to the Visual Agent to draft the maroon and beige layout structure."
        output = f"Hello! I am ready to design your visual experience. I recommend our warm oat beige (#FDFBF7) background paired with Cabernet maroon (#722631) buttons and headers. Let me know your preferred layout style."
    elif to_agent == "Logic Agent":
        status = "Deconstructing technical requirements and preparing code implementation..."
        update = f"I am routing the project to the Logic Agent to engineer the robust algorithmic implementation."
        output = f"Logic Agent initialized. I have reviewed the technical parameters and am synthesizing production-ready, fully-typed code with error bounds."
    elif to_agent == "Creator Agent":
        status = "Crafting narrative storytelling and persuasive brand copy..."
        update = f"I am shifting active context to the Creator Agent to generate compelling copy."
        output = f"Greetings! Creator Agent ready. I am crafting vivid, high-converting copy tailored to your target audience."
    elif to_agent == "Reviewer Agent":
        status = "Executing comprehensive QA audit and validating edge cases..."
        update = f"Handing over to the Reviewer Agent for quality control and proofreading."
        output = f"Reviewer Agent on deck. I am checking test coverage, color contrast compliance, and formatting precision."
    else:
        status = "Architect Agent drafting system hierarchy and phase milestones..."
        update = f"Routing initial project intake to the Architect Agent to map out system modularity and boundaries."
        output = f"Architect Agent standing by. I have established the architectural blueprint and will coordinate handoffs to the downstream specialists."

    ui_command = UICommandBlock(
        from_agent=from_agent,
        to_agent=to_agent,
        status_message=status
    )

    return OrchestrationResponse(
        ui_command=ui_command,
        orchestrator_update=update,
        active_agent=to_agent,
        agent_output=output
    )

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "The Conductor", "theme": "Maroon & Beige"}

if __name__ == "__main__":
    uvicorn.run("server.py:app", host="0.0.0.0", port=8080, reload=True)
