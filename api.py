import gspread
from oauth2client.service_account import ServiceAccountCredentials

def integrando_google_planilha():
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

    resposta = planilha.update_cell(1,1, 'teste')
    print(resposta)

    return resposta

integrando_google_planilha()