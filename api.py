import gspread
from oauth2client.service_account import ServiceAccountCredentials

def integrando_google_planilha(texto):
    #NOTE - integrando_google_planilha
    """
    Integra a planilha do google
    
    params:
        - string: aba_planilha
    
    returns:
        - worksheet: planilha"""
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    gc = gspread.authorize(credentials)
    wks = gc.open_by_key('1bB2cHSv62AuEzBFbwr8haiFK434XKK0DdqE_PfIg580')
    planilha = wks.worksheet('Página1')
    print(f"planilha: {planilha}")    

    with open('linha_planilha.txt', 'r') as arquivo:
        linha_planilha = int(arquivo.read())
    resposta = planilha.update_cell(linha_planilha,1, texto)
    linha_planilha = str(linha_planilha + 1)
    with open('linha_planilha.txt', 'w') as arquivo:
        arquivo.write(linha_planilha)
    print(resposta)

    return resposta