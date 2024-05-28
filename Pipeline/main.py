import optparse
from src.pipeline import run
from dotenv import load_dotenv; load_dotenv()

parser = optparse.OptionParser()
parser.add_option('-t', '--timestamp', dest='timestamp', default='2024-05-01')
''' Parametros de entrada: 
    -t --timestamp : Timestamp do dia que deseja processar
    -example: '2024-05-01' 
    '''

parametros, _ = parser.parse_args()
''' Parametros de entrada '''

if __name__ == "__main__":
    run(parametros.timestamp)