from app.core.shared_state import SharedState

from app.agents.search_agent import SearchAgent
from app.agents.source_classification_agent import SourceClassifyAgent
from app.agents.trust_agent import TrustAgent
from app.agents.verification_agent import VerificationAgent
from app.agents.confidence_agent import ConfidenceAgent


class Coordinator:
    
    def coordinate(self, shared_state: SharedState) -> SharedState:
        shared_state.workflow_status = "Running"
        
        if not shared_state.sources:
            search_agent = SearchAgent()
            shared_state = search_agent.search(shared_state)
        
        source_classify_agent = SourceClassifyAgent()
        shared_state = source_classify_agent.classify(shared_state)
            
        trust_agent = TrustAgent()
        shared_state = trust_agent.evaluate(shared_state)
        
        verification_agent = VerificationAgent()
        shared_state = verification_agent.verify(shared_state)
        
        confidence_agent = ConfidenceAgent()
        shared_state = confidence_agent.calculate(shared_state)
        
        shared_state.workflow_status = "Completed"
        
        return shared_state
            
        

        
    
    

