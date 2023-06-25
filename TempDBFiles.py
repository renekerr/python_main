# Calculate size and generating 'tempdb' files
def tempdbfiles(drive_sizeGB, processors, log_percentage):
    drive_size_no_alertsMB = drive_sizeGB - 1
    file_sizeMB = int((drive_size_no_alertsMB / processors) * 1024)
    log_file_sizeMB = int(((drive_size_no_alertsMB * log_percentage) / 100) * 1024)
    print('-'*100, '\n-- CONFIGURAR LA TEMPDB (COMPROBAR CANTIDAD DE PROCESADORES Y EL ESPACIO DEL DISCO)')
    print('-'*100, '\n-- Drive size = ', drive_sizeGB, 'GB', '\n-- Drive size no alerts = ', drive_size_no_alertsMB, 'GB', '\n-- Processors = ', processors, '\n-- File [.mdf, .ndf] size = ', file_sizeMB, 'MB' ,'\n-- Log file [.ldf] size = ', log_file_sizeMB, 'MB', '\n')

    print("USE [master]\nGO")
    print("ALTER DATABASE [tempdb] MODIFY FILE ( NAME = N'tempdev', SIZE = ", file_sizeMB, "MB, FILEGROWTH = 0 )\nGO",
          sep='')
    for files in range(2, processors + 1):
        print("ALTER DATABASE [tempdb] ADD FILE ( NAME = N'tempdev", files, "', FILENAME = N'E:\DATASQL\DISK2TEMPDB\DATA\\tempdev", files, ".ndf' , SIZE = ", file_sizeMB, "MB , FILEGROWTH = 0)\nGO", sep='')
    print("ALTER DATABASE [tempdb] MODIFY FILE ( NAME = N'templog', SIZE = ", log_file_sizeMB, "MB , FILEGROWTH = 0)\nGO", sep='')

script_generator = tempdbfiles(drive_sizeGB = 10 ,processors = 3, log_percentage = 20)
print(script_generator)



# ------------------------------------------------------------------------------------------------
# -- CONFIGURAR LA TEMPDB (COMPROBAR CANTIDAD DE PROCESADORES Y EL ESPACIO DEL DISCO)
# ------------------------------------------------------------------------------------------------
# /*	Ejemplo:
#
# Disco para la tempdb = 80 GB Total
# # procesadores = 8 (creamos un fichero de tempdb por cada procesador)
#
# Para que no salten alertas por falta de espacio en el disco duro, utilizaremos solamente 75GB para la tempdb.
# (75 GB / 8) * 1024 = 9600MB...para cada uno de los ficheros .mdf y .ndf
#
# Para el fichero del log, vamos a asignar el 20 – 25 % de los 75GB del disco de tempdb
# (75 GB * 25 %) * 1024 = 19200MB, este es el tamaño que va a tener el archivo del log  					*/
#
#
# USE [master]
#
# GO
# ALTER DATABASE [tempdb] MODIFY FILE ( NAME = N'tempdev', SIZE = 2048MB , FILEGROWTH = 0 ) -- a modificar (2560MB)
# GO
# ALTER DATABASE [tempdb] ADD FILE ( NAME = N'tempdev2', FILENAME = N'E:\DATASQL\DISK2TEMPDB\DATA\tempdev2.ndf' , SIZE = 2048MB , FILEGROWTH = 0)
# GO
# ALTER DATABASE [tempdb] ADD FILE ( NAME = N'tempdev3', FILENAME = N'E:\DATASQL\DISK2TEMPDB\DATA\tempdev3.ndf' , SIZE = 2048MB , FILEGROWTH = 0)
# GO
# ALTER DATABASE [tempdb] ADD FILE ( NAME = N'tempdev4', FILENAME = N'E:\DATASQL\DISK2TEMPDB\DATA\tempdev4.ndf' , SIZE = 2048MB , FILEGROWTH = 0)
# GO
# --ALTER DATABASE [tempdb] ADD FILE ( NAME = N'tempdev5', FILENAME = N'E:\DATASQL\DISK2TEMPDB\DATA\tempdev5.ndf' , SIZE = 10240MB , FILEGROWTH = 0)
# --GO
# --ALTER DATABASE [tempdb] ADD FILE ( NAME = N'tempdev6', FILENAME = N'E:\DATASQL\DISK2TEMPDB\DATA\tempdev6.ndf' , SIZE = 10240MB , FILEGROWTH = 0)
# --GO
# --ALTER DATABASE [tempdb] ADD FILE ( NAME = N'tempdev7', FILENAME = N'E:\DATASQL\DISK2TEMPDB\DATA\tempdev7.ndf' , SIZE = 10240MB , FILEGROWTH = 0)
# --GO
# --ALTER DATABASE [tempdb] ADD FILE ( NAME = N'tempdev8', FILENAME = N'E:\DATASQL\DISK2TEMPDB\DATA\tempdev8.ndf' , SIZE = 10240MB , FILEGROWTH = 0)
# --GO
# ALTER DATABASE [tempdb] MODIFY FILE ( NAME = N'templog', SIZE = 2048MB , FILEGROWTH = 0)
# -- Autogrow = 512MB
# -- a modificar 20-25 % de los 75GB del disco de la tempdb
# -- E:\DATASQL\DISK4LOG\LOGSQL\templog.ldf
# GO

