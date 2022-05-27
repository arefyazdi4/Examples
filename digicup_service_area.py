def check_area_cover():
    store_number = int(input())
    covered_area = list()
    for i in range(store_number):
        covered_area.append(tuple(map(int, input().split())))
    start_service_area = int(input())
    end_service_area = int(input())
    service_area = [i+start_service_area for i in range(end_service_area-start_service_area+1)]

    for point in service_area:
        area_state = False
        for start_local_area, end_local_area in covered_area:
            if end_local_area >= point >= start_local_area:
                area_state = True
        if not area_state:
            return 'false'
    return 'true'


if __name__ == '__main__':
    print(check_area_cover())

