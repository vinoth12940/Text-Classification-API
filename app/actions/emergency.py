class AdvancedEmergencyHandler:
    def __init__(self):
        self.priority_map = {
            "MEDICAL": 1,
            "FIRE": 2,
            "CRIME": 3
        }
    
    def handle_emergency(self, analysis: Dict) -> Dict:
        """Enhanced handler using Gemini's risk assessment"""
        action_plan = []
        
        if analysis.get('risk_level') == "CRITICAL":
            action_plan.append({
                "action_type": "AUTO_DISPATCH",
                "services": self._determine_services(analysis),
                "location": analysis.get('location', {}).get('coordinates')
            })
        
        if "medical_keywords" in analysis:
            action_plan.extend([
                self._generate_first_aid(analysis),
                self._alert_medical_contacts(analysis)
            ])
            
        return {
            "status": "PROCESSED",
            "actions": sorted(action_plan, key=lambda x: self.priority_map.get(x['type'], 4))
        }

    def _determine_services(self, analysis: Dict) -> List[str]:
        # Uses Gemini's entity recognition
        return list(set(
            entity['service_type'] 
            for entity in analysis.get('entities', [])
            if entity['type'] == 'EMERGENCY_SERVICE'
        )) 