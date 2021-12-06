
import uuid

    
def generate_prod_code():
    code = str(uuid.uuid4().int).replace('-','')[:10]
    return code    
    
