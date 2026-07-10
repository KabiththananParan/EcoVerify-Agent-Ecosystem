from app.core.shared_state import SharedState

class SearchAgent:
    def search(self, shared_state: SharedState) -> SharedState:
        claim = shared_state.claim
        
        