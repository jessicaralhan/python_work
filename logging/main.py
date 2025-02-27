level_count = {"INFO" : 0, "ERROR" : 0, "WARNING" : 0}

with open("company.log", "r") as log_file:
    for message in log_file:   #1st - 2025-02-27 00:34:57,659 - INFO - File uploaded successfully 
        # print(message)
        for count in level_count:   # 1st - INFO 
            print(count)
            if count in message:    
                level_count[count] += 1    # 1st - INFO : 1, 2nd - ERROR : 1, 3rd - WARNING : 1, 4th - INFO : 2

    print(level_count)
        
    




































# import logging
# # name = 'not working'
# # logging.error('%s raised an error',)

# logging.basicConfig(
#     filename="company.log",
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s"
# )
# logging.info("User logged in")
# logging.error("Database connection failed")
# logging.warning("Disk space low")
# logging.info("File uploaded successfully")
# #log_count = 0
# level_count = {"INFO" : 0, "ERROR" : 0, "WARNING" : 0}

# with open("company.log", "r") as log_file:
#     for message in log_file:   #1st - 2025-02-27 00:34:57,659 - INFO - File uploaded successfully
#         # print(message)
#         for count in level_count:   # 1st - INFO 2nd - Error 3rd - warning
#             # print(count)
#             if count in message:    
#                 level_count[count] += 1    # 1st - INFO : 1, 2nd - ERROR : 1, 3rd - WARNING : 1, 4th - INFO : 2

#     print(level_count)
        
    
