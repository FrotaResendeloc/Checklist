import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
from datetime import datetime

class ChecklistApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Checklist Diário - Resendeloc")
        self.root.configure(bg='#333')

        self.selected_plate = tk.StringVar()
        self.selected_dealer = tk.StringVar()
        self.mileage = tk.StringVar()
        self.auditor = tk.StringVar()
        self.observations = tk.StringVar()

        self.placas = [
    "KRQ-4957", "KRU-9256", "KRU-9265", "KRU-9267", "KRU-9282",
    "KRV-5179", "KRV-5180", "KRV-5182", "KRV-5183", "KRV-5184",
    "KRV-5185", "KRV-5186", "KRV-5B81", "KRW-5936", "KRW-5937",
    "KRX-4645", "KRY-5423", "KRZ-3933", "KRZ-3934", "KRZ-8823",
    "KXQ-8240", "KXQ-8241", "KXQ-8251", "KYQ-9562", "KYQ-9F63",
    "KYZ-9106", "KYZ-9B05", "KZE-8984", "KZE-8985", "KZE-8990",
    "KZE-8991", "KZE-8J82", "KZH-9989", "KZH-9990", "KZH-9991",
    "KZO-8E74", "LMO-9J71", "LMP-2D79", "LMP-3G03", "LMP-6D79",
    "LMQ-0A16", "LMS-5I96", "LMS-5I97", "LMS-5I99", "LMS-5J00",
    "LMS-5J04", "LMS-5J05", "LMU-1G93", "LMV-9G90", "LMV-9G99",
    "LMV-9H16", "LMV-9H24", "LMV-9H25", "LMV-9H27", "LMV-9H31",
    "LMV-9H34", "LMV-9H35", "LMW-0H57", "LMW-1C40", "LMW-1C64",
    "LMW-1C73", "LMW-1C81", "LMW-1C85", "LMW-7B25", "LMW-7B65",
    "LMW-7B71", "LMW-7B74", "LMW-7J90", "LMW-9D58", "LMW-9D61",
    "LMX-0B17", "LMY-0A17", "LMY-0B50", "LNH-6J93", "LNH-7D34",
    "LNM-3G87", "LNR-1J01", "LOE-1F76", "LOG-5C90", "LRJ-3H61",
    "LRJ-3H62", "LRJ-3H63", "LRJ-3J01", "LRJ-6C68", "LRO-4C92",
    "LSI-8009", "LSI-9201", "LSI-9C03", "LSJ-7443", "LSR-7522",
    "LSV-9882", "LSW-8930", "LSW-8963", "LSW-8965", "LSY-3449",
    "LSY-3450", "LSY-3451", "LSY-3452", "LSY-3453", "LSY-7891",
    "LTA-1557", "LTA-1560", "LTA-1561", "LTB-7371", "LTB-7372",
    "LTB-7374", "LTC-6048", "LTE-2289", "LTI-3035", "LTI-3036",
    "LTI-3038", "LTI-3039", "LTI-3040", "LTI-3041", "LTI-3A40",
    "LTL-7783", "LTL-7784", "LTL-7785", "LTL-8332", "LTL-9498",
    "LTL-9500", "LTM-8D44", "LTM-8I79", "LTM-8I80", "LTO-7F57",
    "LTO-7F58", "LTO-7F60", "LTO-7F63", "LTO-7F65", "LTO-7F66",
    "LTO-7F67", "LTO-7F69", "LTO-7F70", "LTO-7F78", "LTO-7F79",
    "LTO-7F80", "LTQ-3H04", "LTQ-3H10", "LTQ-3H11", "LTQ-3H12",
    "LTQ-3H13", "LTQ-3H15", "LTQ-3H23", "LTQ-3H24", "LTQ-3H26",
    "LTQ-3H27", "LTR-9I68", "LTR-9I70", "LTR-9I74", "LTR-9I79",
    "LTR-9I80", "LTR-9I81", "LTR-9I83", "LTS-1F84", "LTS-1G01",
    "LTS-1H31", "LTS-1H42", "LTS-2A91", "LTS-2A92", "LTS-2A93",
    "LTS-2D54", "LTS-4A04", "LTS-4A24", "LTS-4A25", "LTS-4J24",
    "LTS-4J26", "LTS-4J31", "LTV-7A44", "LTX-7D86", "LTX-7J05",
    "LUA-1B96", "LUB-7I90", "LUD-7C01", "LUD-7H94", "LUD-7H98",
    "LUF-7D44", "LUF-7D45", "LUH-7G08", "LUH-7I97", "LUH-7J14",
    "LUJ-7I07", "LUL-8C69", "LUP-8E53", "LUQ-1D36", "LUR-7H82",
    "LUR-8B78", "LUS-9F99", "LUT-5G85", "LUT-6C31", "RIP-0J32",
    "RIP-0J42", "RIP-0J63", "RIP-0J71", "RIP-1A42", "RIP-3C49",
    "RIP-3D78", "RIP-3D82", "RIQ-0H49", "RIQ-0H54", "RIQ-0H62",
    "RIQ-0H73", "RIQ-2F64", "RIQ-2G52", "RIR-1D53", "RIR-1D55",
    "RIR-1D57", "RIR-1D58", "RIR-1D66", "RIR-1D68", "RIR-1D69",
    "RIR-1D70", "RIR-1D73", "RIR-1D76", "RIR-1D77", "RIR-1D79",
    "RIR-1D81", "RIR-1D82", "RIR-1D83", "RIR-1D84", "RIR-1J32",
    "RIR-2G68", "RIR-2G72", "RIY-1D04", "RIY-1D09", "RIY-1D27",
    "RIY-1D32", "RIY-1D51", "RIY-1D59", "RIY-1D67", "RJB-4F99",
    "RJB-4G02", "RJB-4G03", "RJB-4G04", "RJB-4G06", "RJB-4G07",
    "RJC-1F18", "RJC-3H83", "RJD-0J05", "RJD-1E77", "RJD-1E80",
    "RJD-1E84", "RJD-1E90", "RJD-8J32", "RJE-8I14", "RJE-8I25",
    "RJE-8I27", "RJE-8I30", "RJE-8I31", "RJG-1A58", "RJG-1A59",
    "RJG-1A60", "RJG-1A61", "RJG-1A63", "RJG-1A66", "RJG-1A67",
    "RJG-1A68", "RJG-1A69", "RJG-1A70", "RJG-1A71", "RJG-1A72",
    "RJG-1A73", "RJG-1A74", "RJG-1A76", "RJG-1A78", "RJG-1A79",
    "RJG-1A81", "RJG-1A82", "RJG-1A83", "RJG-1A86", "RJG-1A87",
    "RJG-1A88", "RJG-1A89", "RJG-1A90", "RJG-1A91", "RJG-2C61",
    "RJG-2C80", "RJH-1B33", "RJH-1B34", "RJH-1B35", "RJH-1B37",
    "RJH-1B39", "RJH-1B40", "RJH-1B41", "RJH-1B43", "RJH-1B44",
    "RJH-1B45", "RJH-1B46", "RJH-1B48", "RJH-1B50", "RJH-1B51",
    "RJH-1B52", "RJH-1B60", "RJH-1B64", "RJH-1B70", "RJH-1B73",
    "RJH-1B75", "RJH-1B76", "RJH-1B77", "RJH-1B79", "RJH-1B82",
    "RJH-1B83", "RJH-1B84", "RJH-1B87", "RJH-1B88", "RJH-1B89",
    "RJH-1B90", "RJH-2F93", "RJH-2F98", "RJH-2G00", "RJH-2G02",
    "RJH-9C56", "RJH-9C58", "RJH-9C61", "RJH-9C62", "RJH-9C64",
    "RJH-9H43", "RJH-9H44", "RJI-1D48", "RJI-1D52", "RJI-2G72",
    "RJJ-1B80", "RJJ-1B83", "RJJ-1B85", "RJJ-1B86", "RJJ-1B88",
    "RJJ-1B90", "RJJ-1C14", "RJJ-1C15", "RJJ-1C18", "RJJ-1C21",
    "RJJ-1C22", "RJJ-1C26", "RJJ-9D18", "RJJ-9D26", "RJL-5I10",
    "RJL-5I11", "RJL-5I14", "RJL-5I16", "RJM-1J83", "RJM-1J89",
    "RJM-1J92", "RJM-1J95", "RJM-1J99", "RJN-2B28", "RJN-2B39",
    "RJN-2B57", "RJN-9C53", "RJN-9C55", "RJN-9C56", "RJO-0G57",
    "RJO-0G62", "RJO-0G69", "RJO-0G71", "RJO-0G73", "RJO-0G78",
    "RJO-1H09", "RJO-1H21", "RJR-0I85", "RJR-0I94", "RJR-0I99",
    "RJU-0I43", "RJU-0I46", "RJU-0I50", "RJU-0I51", "RJU-0I52",
    "RJU-0I53", "RJU-0I55", "RJU-0I56", "RJU-0I58", "RJU-0I59",
    "RJX-0H61", "RJX-0H65", "RJY-0G67", "RJY-0G74", "RJY-0G78",
    "RJY-0G82", "RJY-0G84", "RJY-0G87", "RJY-0G89", "RJY-0G94",
    "RJY-0G96", "RJY-0G97", "RJY-0G98", "RJY-0H14", "RJY-0H18",
    "RJY-0H22", "RJZ-2C80", "RJZ-2C85", "RJZ-2D03", "RJZ-8I04",
    "RKA-5B23", "RKA-5B36", "RKA-5B37", "RKA-5B38", "RKB-8F30",
    "RKC-0J89", "RKC-0J98", "RKE-1F31", "RKE-1F36", "RKE-1F54",
    "RKE-1F55", "RKF-1E34", "RKF-1E38", "RKF-1E44", "RKF-1E47",
    "RKF-1E48", "RKF-1E50", "RKF-1E53", "RKF-1E57", "RKF-1E59",
    "RKF-1E61", "RKG-0J55", "RKH-0J92", "RKH-0J99", "RKH-1A00",
    "RKH-1A04", "RKH-1A11", "RKH-1A19", "RKH-1A21", "RKH-1A23",
    "RKH-1A29", "RKH-1A41", "RKH-1A42", "RKH-1A48", "RKH-1A49",
    "RKH-1A50", "RKH-1A53", "RKH-1A54", "RKH-1A55", "RKH-1A59",
    "RKH-1A60", "RKH-1A61", "RKH-1A62", "RKH-1A68", "RKH-1A71",
    "RKH-1A74", "RKH-1A77", "RKH-1A80", "RKH-1A83", "RKH-1A84",
    "RKH-1A89", "RKH-1A97", "RKH-1B23", "RKK-1A58", "RKM-2G31",
    "RKM-2G50", "RKM-2G53", "RKM-2G58", "RKM-2G65", "RKM-2G69",
    "RKQ-1E69", "RKR-0G09", "RKR-0G14", "RKR-0G15", "RKR-0G17",
    "RKR-0G23", "RKR-0G25", "RKR-0G32", "RKR-0G38", "RKR-0G41",
    "RKR-0G43", "RKR-0G44", "RKR-0G45", "RKR-0G46", "RKR-0G49",
    "RKR-0G52", "RKR-0G53", "RKR-0G55", "RKR-0G57", "RKR-0G59",
    "RKR-0G62", "RKR-0G65", "RKR-0G67", "RKR-0G68", "RKR-0G70",
    "RKR-0G72", "RKR-0G73", "RKR-0G75", "RKR-0G76", "RKR-0G77",
    "RKR-0G80", "RKR-0G84", "RKR-0G87", "RKR-0G95", "RKR-0G97",
    "RKR-0H03", "RKU-1H32", "RKU-1H37", "RKV-4B31"
]

        self.revendas = [
    "AGAPE - FEIRA DE SANTANA",
    "ANGKOR - JACAREÍ",
    "ANTUERPIA - CARUARU",
    "ARDENAS - PORTO VELHO",
    "BAVIERA - PORTO ALEGRE",
    "BERE - SÃO MIGUEL",
    "BOTELLA - OSASCO",
    "BRUGUES  - RIO VERDE",
    "BRUXELAS  - APARECIDA DE GOIANIA",
    "BS SÃO GONÇALO - SÃO GONÇALO",
    "CARAGUA DE SINOP - SINOP",
    "CELERITAS CURITIBA - CASCAVEL",
    "CELERITAS CURITIBA - CURITIBA",
    "CELERITAS LONDRINA  - LONDRINA",
    "CELERITAS MARINGA - MARINGA",
    "COLISEU - PETROPOLIS",
    "COLOSSUS - CORDOVIL",
    "CONQUISTA - VITORIA DA CONQUISTA",
    "COROA DO VALE - JUAZEIRO",
    "DESCOBRIMENTO - PORTO SEGURO  - PORTO SEGURO",
    "DISCERNIMENTO - SÃO LUIS",
    "ESTRELA DE NATAL - NATAL",
    "F. DANTAS - MACAPÁ - MACAPA",
    "FRANCOSP - FRANCO DA ROCHA",
    "GALLIA - MOGI GUAÇU",
    "GANTE - CASCAVEL",
    "HEQET - DIADEMA",
    "HONG KONG - MACEIO",
    "IMPERATRIZ  - IMPERATRIZ",
    "IMPERATRIZ - IMPERATRIZ",
    "IMPERIO AMADO - ILHEUS - ILHEUS",
    "IMPERIO DA VITORIA - VITORIA",
    "ITAMARACA - JOAO PESSOA",
    "JALAPÃO - PALMAS",
    "KANNA - JABOATÃO",
    "KHMER - TAUBATE",
    "LEAR BAHIA - SALVADOR",
    "LIEGE  - BRASILIA",
    "LIMOGES DO AMAZONAS - MANAUS",
    "MACEDONIA - CAMPO GRANDE",
    "MADRI - ANGRA DOS REIS",
    "MAHAL - CORDOVIL - AS",
    "MAJESTIC - PIRITUBA",
    "MARABA NOVA BELEM - MARABA",
    "MARSELHA - PICOS",
    "MEGA  - DUQUE DE CAXIAS",
    "MEGA - DUQUE DE CAXIAS",
    "MESO - SÃO MATEUS",
    "MESTRIA - VILA PRUDENTE - MOOCA",
    "MOGI DISTRIBUIDORA  - MOGI DAS CRUZES",
    "MONS - RONDONÓPOLIS",
    "NAVI - ESPLENDIDA - COTIA",
    "NAVI - SUBLIME - COTIA",
    "NIAGARA - CACHOEIRO DE ITAPEMIRIM",
    "NOVA BELEM - BELEM",
    "PLACAR - DUQUE DE CAXIAS",
    "REALEZA - MAGE",
    "REDENTOR - BARRA MANSA",
    "REI DO VALLE - PETROLINA",
    "RODES - CABO FRIO",
    "RRS - CUIABA",
    "SANTO ARNOLDO - FORTALEZA",
    "SETE CIDADES - TERESINA",
    "SOBERANO JUNDIAI - JUNDIAI",
    "TAP HOUSE - INTERLAGOS",
    "VILA LEOPOLDINA - SÃO PAULO - CENTRO",
    "XANTEN - ARACAJU",
    "ZNORTESP - PARQUE NOVO MUNDO"
]

        # Componentes do formulário
        label_plate = ttk.Label(root, text="Placa:", background='#333', foreground='#fff')
        label_plate.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.combo_plate = ttk.Combobox(root, textvariable=self.selected_plate, values=self.placas)
        self.combo_plate.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        label_dealer = ttk.Label(root, text="Revenda:", background='#333', foreground='#fff')
        label_dealer.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.combo_dealer = ttk.Combobox(root, textvariable=self.selected_dealer, values=self.revendas)
        self.combo_dealer.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        label_mileage = ttk.Label(root, text="Quilometragem:", background='#333', foreground='#fff')
        label_mileage.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_mileage = ttk.Entry(root, textvariable=self.mileage)
        self.entry_mileage.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        label_auditor = ttk.Label(root, text="Auditor:", background='#333', foreground='#fff')
        label_auditor.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_auditor = ttk.Entry(root, textvariable=self.auditor)
        self.entry_auditor.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        label_checklist = ttk.Label(root, text="Checklist (OK/NOK):", background='#333', foreground='#fff')
        label_checklist.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)

        # Lista de itens do checklist
        self.checklist_items = ["Nível de óleo do motor", "Nível de água do radiador", "Elétrica", "Pneus/Rodas", "Funilaria"]
        self.checklist_vars = []
        for i, item in enumerate(self.checklist_items):
            var = tk.StringVar(value="OK")
            self.checklist_vars.append(var)
            label_item = ttk.Label(root, text=item + ":", background='#333', foreground='#fff')
            label_item.grid(row=4+i, column=0, padx=5, pady=2, sticky=tk.W)
            radio_ok = ttk.Radiobutton(root, text="OK", variable=var, value="OK", style='Dark.TRadiobutton')
            radio_ok.grid(row=4+i, column=1, padx=5, pady=2, sticky=tk.W)
            radio_nok = ttk.Radiobutton(root, text="NOK", variable=var, value="NOK", style='Dark.TRadiobutton')
            radio_nok.grid(row=4+i, column=2, padx=5, pady=2, sticky=tk.W)

        label_observations = ttk.Label(root, text="Observações:", background='#333', foreground='#fff')
        label_observations.grid(row=9, column=0, padx=5, pady=5, sticky=tk.W)
        self.text_observations = tk.Text(root, width=30, height=5, wrap=tk.WORD)
        self.text_observations.grid(row=9, column=1, columnspan=2, padx=5, pady=5, sticky=tk.W)

        # Botão de envio
        submit_button = ttk.Button(root, text="Enviar", command=self.submit_form)
        submit_button.grid(row=10, column=0, columnspan=3, padx=5, pady=10)

        # Estilo para os RadioButtons
        style = ttk.Style()
        style.configure('Dark.TRadiobutton', background='#333', foreground='#fff')

    def submit_form(self):
        # Obter os valores do formulário
        plate = self.selected_plate.get()
        dealer = self.selected_dealer.get()
        mileage = self.mileage.get()
        auditor = self.auditor.get()
        observations = self.text_observations.get("1.0", tk.END).strip()

        # Obter a data atual
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Obter o resultado do checklist
        checklist_result = [var.get() for var in self.checklist_vars]

        # Salvar os dados em um arquivo CSV
        self.save_to_csv(current_date, plate, dealer, mileage, auditor, observations, checklist_result)

        # Limpar os campos do formulário após o envio
        self.clear_form()

        # Exibir uma mensagem de confirmação
        messagebox.showinfo("Sucesso", "Formulário enviado com sucesso! Nós da Resendeloc e a sua segurança, agradecemos. Um ótimo dia de serviço!")

    def save_to_csv(self, date, plate, dealer, mileage, auditor, observations, checklist_result):
        # Verificar se o arquivo já existe
        file_exists = False
        try:
            with open('checklist.csv', 'r') as f:
                file_exists = True
        except FileNotFoundError:
            pass

        # Adicionar os dados ao arquivo CSV
        with open('checklist.csv', 'a') as f:
            # Adicionar cabeçalho se o arquivo não existir
            if not file_exists:
                f.write('Data,Placa,Revenda,Quilometragem,Auditor,Observações,' + ','.join(self.checklist_items) + '\n')
            
            # Escrever os dados do formulário
            f.write(f'{date},{plate},{dealer},{mileage},{auditor},{observations},{",".join(checklist_result)}\n')

    def clear_form(self):
        # Limpar os campos do formulário
        self.selected_plate.set('')
        self.selected_dealer.set('')
        self.mileage.set('')
        self.auditor.set('')
        self.text_observations.delete('1.0', tk.END)
        for var in self.checklist_vars:
            var.set('OK')

if __name__ == "__main__":
    root = tk.Tk()
    app = ChecklistApp(root)
    root.mainloop()
