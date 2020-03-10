from enum import Enum

class LogLineType(Enum):
    START = 0
    STOP = 1
    RUNNING = 2
    INFO = 3
    
    @staticmethod
    def get_line_type(type_text: str) -> str:
        if type_text in ['Start', 'Stop', 'Running' , 'Info']:
            return LogLineType[type_text.upper()]
        
        sv_2_en_trans = {'Start': 'Start','Stopp': 'Stop','Pågående': 'Running', 'Info': 'Info'}
        
        return LogLineType[sv_2_en_trans[type_text].upper()]
