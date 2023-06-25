# Kerberos request (using a dictionary)

# Standalone server
items = {'server' : 'SRDWDES-01'}

# Cluster
#items = {'server01': 'SRDPISQLPRO-01', 'server02':'SRDPISQLPRO-02', 'listener': 'SRDPISQL-PRO'}
user ='admindata'

for n in items.values():
    print('--', n, '\n# Asignamos SPN de Usuario')
    print("Set-ADUser -Identity ", user, " -ServicePrincipalNames @{Add = 'MSSQLSvc/", n, ".mutua.es','MSSQLSvc/", n, ".mutua.es:1433'}", "\n", sep='')

    print('# Asignamos SPN de Servidor')
    print("Get-ADComputer -Identity ", n, "| Set-ADObject -Add @{'msDS-AllowedToDelegateTo'=@('MSSQLSvc/", n, ".mutua.es','MSSQLSvc/", n, ".mutua.es:1433')}", "\n", sep='')



# -- Habilitar KERBEROS para URL
# setspn -s http/srpbirepsql-pre.mutua.es mutua\adminreport
# setspn -s http/srpbirepsql-pre.mutua.es:1433 mutua\adminreport




