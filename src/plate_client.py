
import requests
from models.plate_reader import PlateReader, InvalidImage
from io import BytesIO

plate_reader = PlateReader.load_from_file('./model_weights/plate_reader_model.pth')

class PlateClient:
    def __init__(self, url: str):
        self.url = url
    
    def readNumber(self, id: str):
        response = requests.get(f'{self.url}/{id}')
        if response.ok:
            try:
                #im = response.content
                im = BytesIO(response.content)
                res = plate_reader.read_text(im)
            except InvalidImage:
                return 400, f'invalid image {id}'
            return 200, res
        elif response.status_code == 404:
            return response.status_code, f'image {id} not found'
        else:
            return response.status_code, f'error finding image {id} {response.status_code} {response.reason}' 

    def readNumbers(self, ids: str):
        idsl=ids.split()
        #return 200, ids
        res=[]
        for id in idsl:
            status, resid = self.readNumber(id)
            if status==200:
                res.append({id:resid})
            else:
                return status, resid
        return 200, res
        