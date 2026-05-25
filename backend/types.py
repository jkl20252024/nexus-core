from typing import Dict, Any

Lead = Dict[str, Any]
Research = Dict[str, Any]

class PipelineResult:
    def __init__(self, lead: Lead, research: Research):
        self.lead = lead
        self.research = research