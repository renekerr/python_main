# Data base information
# https://www.sqlshack.com/sql-server-transaction-log-administration-best-practices/#:~:text=Although%20there%20is%20no%20one,your%20database%20growth%20plan%20can

def db_info(db_name, secondaryfilegroup, db_size_GB, ndf_files, db_prctg_growth, log_prctg_growth, log_initial_size):
    initial_size = int(db_size_GB/(ndf_files + 1)) * 1024
    db_maxsize = int((db_size_GB * 1024) + ((db_size_GB * 1024) * db_prctg_growth/100))
    file_size = int(db_maxsize / db_size_GB)
    log_file_sizeMB = int((db_size_GB * 1024) + ((db_size_GB * 1024) * log_prctg_growth/100))
    log_fixed_maxsize = 10240
    file_growth = 512
    print('-- Database name :           ', db_name)
    print('-- Database size :           ', db_size_GB, 'GB')
    print('-- Growth percentage :       ', db_prctg_growth, '%\n')
    print('-- NDF files :               ', ndf_files)
    print('-- Secondary filegroup :     ', secondaryfilegroup)
    print('-- Initial size :            ', initial_size, 'MB')
    print('-- Maxsize :                 ', db_maxsize, 'MB')
    print('-- File maxsize MDF&NDF :    ', file_size, 'MB\n')
    print('-- Log initial size :        ', log_initial_size, 'MB')
    print('-- Log maxsize :             ', log_file_sizeMB, 'MB')
    print('-- Log maxsize fixed :       ', log_fixed_maxsize, 'MB\n')
    print('-- Filegrowth :              ', file_growth, 'MB')

database_info = db_info(db_name = 'DM_IFRS17', secondaryfilegroup = 'DATAUSER', db_size_GB = 4, ndf_files = 3, db_prctg_growth = 10, log_prctg_growth = 30, log_initial_size = 512)
print(database_info)















