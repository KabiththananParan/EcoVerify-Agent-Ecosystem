from app.core.shared_state import SharedState


class Coordinator():
    
    def coordinate(self, shared_state: SharedState) -> SharedState:
        shared_state.workflow_status = "Running"
        
        if not shared_state.sources:
            Search_Agent()
        
    
    

