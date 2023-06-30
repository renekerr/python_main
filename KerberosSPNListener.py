# Kerberos request (using a dictionary)

# Standalone server
items = {'server' : 'server_name'}

# Cluster
#items = {'server01': 'server_name_01', 'server02':'server_name_02', 'listener': 'listener_name'}
user ='user_account'

for n in items.values():
    print('--', n, '\n# Asignamos SPN de Usuario')
    print("Set-ADUser -Identity ", user, " -ServicePrincipalNames @{Add = 'MSSQLSvc/", n, ".mutua.es','MSSQLSvc/", n, ".mutua.es:1433'}", "\n", sep='')

    print('# Asignamos SPN de Servidor')
    print("Get-ADComputer -Identity ", n, "| Set-ADObject -Add @{'msDS-AllowedToDelegateTo'=@('MSSQLSvc/", n, ".mutua.es','MSSQLSvc/", n, ".mutua.es:1433')}", "\n", sep='')



# -- Habilitar KERBEROS para URL
# setspn -s http/servername.domain.es domain\user
# setspn -s http/servername.domain.es:1433 domain\user




