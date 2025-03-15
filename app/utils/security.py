from typing import Optional

class InputValidator:
    @staticmethod
    def validate_message(text: str) -> Optional[str]:
        """Returns None if valid, error message if not"""
        if len(text) > 2000:
            return "Message too long (max 2000 chars)"
            
        if re.search(r'(?:http|ftp|https)://', text):
            return "Links not allowed"
            
        if any(cmd in text.lower() for cmd in ['sudo', 'rm', 'drop table']):
            return "Potentially dangerous content"
            
        return None 