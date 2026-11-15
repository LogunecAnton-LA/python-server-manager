def menu():
    print("1 - Serverliste zeigen\n2 - Einen neuen Server hinzufuegen\n3 - Einen Server loeschen\n4 - Ausgang")
servers = {
    1: "Berlin-01",
    2: "Muenchen-02",
    3: "Frankfurt-03"
}
server_pool = {
    1: "Naumburg-04",
    2: "Magdeburg-05",
    3: "Halle-06"
} 
while True:
    input("\nEnter, um ein Menu anzuzeigen: ")
    menu()
    number = int(input("\nWählen Sie bitte eine Zahl aus: "))
    if number == 1:
        for number, server in servers.items():
            print(f"[{number}] {server}")
        print("-" * 30)
    elif number == 2:
        print("\nVerfügbare Server zum Hinzufügen:")
        for number, name in server_pool.items():
            print(f"[{number}] {name}")
        if not server_pool:
            print("\nDiese Serverliste ist leer!")
        else:
            server_add = int(input("Weahlen Sie sich einen Server zum Hinzufuegen aus: "))
            number_add = max(servers.keys(), default=0) + 1
            if server_add in server_pool:
                server_name = server_pool[server_add]
                servers[number_add] = server_name
                del server_pool[server_add]
                print(f"{server_name} wurde unter Nummer {number_add} hinzugefuegt!")
            else:
                print("Diese Nummer gibt es nicht im Pool!")
                continue
    elif number == 3:
        for number, server in servers.items():
            print(f"[{number}] {server}")
        print("-" * 30)
        serverweg = int(input("\nWeahlen Sie bitte einen Server zum Loeschen aus: "))
        servers_add1 = max(server_pool.keys(), default=0) + 1
        if serverweg in servers:
            server_name2 = servers[serverweg]
            server_pool[servers_add1] = server_name2
            del servers[serverweg]
            print("Server wurde erfolgreich geloescht!")
        else:
            print("Kein Server wurde geloescht")
        for number, server in servers.items():
            print(f"[{number}] - {server}")
        print("-" * 30)
    elif number == 4:
        print("Aufwiedersehen!")
        break
    else:
        print("Unbekannte Aktion")

        
