coord, hod = input().split("-")
start_coord = int(coord[0], 18)
end_coord = int(coord[1], 18)
start_hod = int(hod[0],18)
end_hod = int(hod[1], 18)
dx = abs(start_hod - start_coord)
dy = abs(end_coord - end_hod)
if dx == 2 and dy == 1 or dx == 1 and dy == 2:
    print("Верно")
else: 
    print("Неверно")