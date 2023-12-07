import tkinter as tk
from tkinter import ttk, font, messagebox
import pyodbc 
import joblib
import pandas as pd
from tkcalendar import DateEntry
from datetime import datetime
import joblib

class ConnectDB:
    def __init__(self):
        server = 'BANGOC'
        database = 'HotelBooking'
        username = 'sa'
        password = '123456'
        global conn_str
        conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'



class GiaoDien:
    def __init__(self):
        self.root = tk.Tk()
        self.root.state('zoomed')
        self.root.title('Nhóm 1')
        
        # Tạo font cho tiêu đề và văn bản
        font_header = font.Font(family='Srisakdi', size=32, weight='bold')
        font_text = font.Font(family='Dancing Script', size=18)
        
        self.label = tk.Label(self.root, text='Nhóm 1', font=font_header)
        self.label.grid(row=0, column=0,columnspan=3,sticky='n')
        
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=1, column=0)
        
        # bảng thông tin khách hàng
        self.frame_Custome = tk.Frame(self.frame)
        self.frame_Custome.grid(row=0,column=0,sticky="n",padx=20)
        
        self.lable_Custome = tk.Label(self.frame_Custome,text='Thông tin khách hàng', font= font_text)
        self.lable_Custome.grid(row=0,column=0,columnspan=2)
        # người đi cùng
        self.label_adults = tk.Label(self.frame_Custome, text='Số người lớn', font=font_text)
        self.label_adults.grid(row=1, column=0)
        self.entry_adults = tk.Entry(self.frame_Custome, font=font_text, width=15)
        self.entry_adults.grid(row=1, column=1)
        self.adults_value = tk.StringVar()
        self.entry_adults.config(textvariable=self.adults_value)

        self.label_children = tk.Label(self.frame_Custome, text='Số trẻ em', font=font_text)
        self.label_children.grid(row=2, column=0)
        self.entry_children = tk.Entry(self.frame_Custome, font=font_text, width=15)
        self.entry_children.grid(row=2, column=1)
        self.children_value = tk.StringVar()
        self.entry_children.config(textvariable=self.children_value)
        # Khách quen
        self.label_is_repeated_guest = tk.Label(self.frame_Custome, text='Đã từng đến', font=font_text)
        self.label_is_repeated_guest.grid(row=4, column=0)
        self.is_repeated_guest_value = tk.StringVar()
        self.is_repeated_guest_combo = ttk.Combobox(self.frame_Custome, textvariable=self.is_repeated_guest_value, values=['Có', 'Không'], font=font_text, width=14, height=30)
        self.is_repeated_guest_combo.grid(row=4, column=1)
        # Loại khách
        self.label_customer_type = tk.Label(self.frame_Custome, text='Loại', font=font_text)
        self.label_customer_type.grid(row=6, column=0)
        customer_types = ['Transient', 'Contract', 'Transient-Party', 'Group']
        self.customer_type_value = tk.StringVar()
        self.customer_type_combo = ttk.Combobox(self.frame_Custome, textvariable=self.customer_type_value, values=customer_types,font=font_text, width=14,height=30)
        self.customer_type_combo.grid(row=6, column=1)
        # quốc gia
        self.label_country = tk.Label(self.frame_Custome, text='Quốc gia', font=font_text)
        self.label_country.grid(row=5, column=0)
        
        countries = ['Bồ Đào Nha', 'Vương quốc Anh', 'Hoa Kỳ', 'Tây Ban Nha', 'Ireland', 'Pháp', 'Không rõ', 'Romania', 'Na Uy', 'Oman', 'Argentina', 'Ba Lan',
            'Đức', 'Bỉ', 'Thụy Sĩ', 'Trung Quốc', 'Hy Lạp', 'Ý', 'Hà Lan', 'Đan Mạch', 'Nga', 'Thụy Điển', 'Úc', 'Estonia', 'Cộng hòa Séc', 'Brasil', 'Phần Lan',
            'Mozambique', 'Botswana', 'Luxembourg', 'Slovenia', 'Albania', 'Ấn Độ', 'Trung Quốc', 'Mexico', 'Maroc', 'Ukraina', 'San Marino', 'Latvia',
            'Puerto Rico', 'Serbia', 'Chile', 'Áo', 'Belarus', 'Lithuania', 'Thổ Nhĩ Kỳ', 'Nam Phi', 'Angola', 'Israel', 'Quần đảo Cayman', 'Zambia', 
            'Cape Verde', 'Zimbabwe', 'Algeria', 'Hàn Quốc', 'Costa Rica', 'Hungary', 'Các Tiểu vương quốc Ả Rập Thống nhất', 'Tunisia', 'Jamaica', 
            'Croatia', 'Hồng Kông', 'Iran', 'Georgia', 'Andorra', 'Gibraltar', 'Uruguay', 'Jersey', 'Trung Phi', 'Cyprus', 'Colombia', 'Guernsey', 'Kuwait',
            'Nigeria', 'Maldives', 'Venezuela', 'Slovakia', 'Fiji', 'Kazakhstan', 'Pakistan', 'Indonesia', 'Lebanon', 'Philippines', 'Senegal', 'Seychelles', 
            'Azerbaijan', 'Bahrain', 'New Zealand', 'Thailand', 'Dominican Republic', 'North Macedonia', 'Malaysia', 'Armenia', 'Nhật Bản', 'Sri Lanka', 
            'Cuba', 'Cameroon', 'Bosnia and Herzegovina', 'Mauritius', 'Comoros', 'Suriname', 'Uganda', 'Bulgaria', 'Ivory Coast', 'Jordan', 'Syria', 
            'Singapore', 'Burundi', 'Saudi Arabia', 'Việt Nam', 'Palau', 'Qatar', 'Egypt', 'Peru', 'Malta', 'Malawi', 'Ecuador', 'Madagascar', 'Iceland', 
            'Uzbekistan', 'Nepal', 'Bahamas', 'Macau', 'Togo', 'Taiwan']
        self.country_value = tk.StringVar()
        self.country_combo = ttk.Combobox(self.frame_Custome, textvariable=self.country_value, values=countries,font=font_text,width=14,height=30)
        self.country_combo.grid(row=5, column=1)     
        # trạng thái đặt phòng trong quá khứ                 
        self.label_previous_cancellations = tk.Label(self.frame_Custome, text='Số lần từng hủy', font=font_text)
        self.label_previous_cancellations.grid(row=7, column=0)
        self.entry_previous_cancellations = tk.Entry(self.frame_Custome, font=font_text,width=15)
        self.entry_previous_cancellations.grid(row=7, column=1)
        self.previous_cancellations_value = tk.StringVar()
        self.entry_previous_cancellations.config(textvariable=self.previous_cancellations_value)

        self.label_previous_bookings_not_canceled = tk.Label(self.frame_Custome, text='Số làn đặt phòng thành công', font=font_text)
        self.label_previous_bookings_not_canceled.grid(row=8, column=0)
        self.entry_previous_bookings_not_canceled = tk.Entry(self.frame_Custome, font=font_text,width=15)
        self.entry_previous_bookings_not_canceled.grid(row=8, column=1)
        self.previous_bookings_not_canceled_value = tk.StringVar()
        self.entry_previous_bookings_not_canceled.config(textvariable=self.previous_bookings_not_canceled_value)
        
        # bảng thông tin phòng
        self.frame_Date = tk.Frame(self.frame)
        self.frame_Date.grid(row=0,column=1,sticky="n",padx=20)
        # thời gian khách dặt phòng 
        self.label_Date = tk.Label(self.frame_Date,text='Thông tin phòng đặt', font= font_text)
        self.label_Date.grid(row=0,column=0,columnspan=2)
        self.label_arrival_date = tk.Label(self.frame_Date, text='Ngày đến', font=font_text)
        self.label_arrival_date.grid(row=1, column=0)
        self.entry_arrival_date = DateEntry(self.frame_Date,font = font_text,width = 15)
        self.entry_arrival_date.grid(row=1, column=1)
        self.arrival_date_value = tk.StringVar()
        self.entry_arrival_date.config(textvariable=self.arrival_date_value)
        
        self.label_BookingDate = tk.Label(self.frame_Date, text='Ngày đặt phòng', font=font_text)
        self.label_BookingDate.grid(row=2, column=0)
        self.entry_BookingDate = DateEntry(self.frame_Date,font = font_text,width = 15)
        self.entry_BookingDate.grid(row=2, column=1)
        self.BookingDate_value = tk.StringVar()
        self.entry_BookingDate.config(textvariable=self.BookingDate_value)
        
        self.label_TotalNights = tk.Label(self.frame_Date, text='Tổng số đêm ở', font=font_text)
        self.label_TotalNights.grid(row=3, column=0)
        self.entry_TotalNights = tk.Entry(self.frame_Date, font=font_text, width=15)
        self.entry_TotalNights.grid(row=3, column=1)
        self.TotalNights_value = tk.StringVar()
        self.entry_TotalNights.config(textvariable=self.TotalNights_value)
        # loại phòng
        self.label_reserved_room_type = tk.Label(self.frame_Date, text='Loại phòng', font=font_text)
        self.label_reserved_room_type.grid(row=4, column=0)
        room_types = ['C', 'A', 'D', 'E', 'G', 'F', 'H', 'L', 'P', 'B']
        self.reserved_room_type_value = tk.StringVar()
        self.room_type_combo = ttk.Combobox(self.frame_Date, textvariable=self.reserved_room_type_value, values=room_types,font=font_text, width=14, height =30)
        self.room_type_combo.grid(row=4, column=1)  
        # giá
        self.label_adr = tk.Label(self.frame_Date, text='Giá chi trả', font=font_text)
        self.label_adr.grid(row=5, column=0)
        self.entry_adr = tk.Entry(self.frame_Date, font=font_text, width=15)
        self.entry_adr.grid(row=5, column=1)
        self.adr_value = tk.StringVar()
        self.entry_adr.config(textvariable=self.adr_value)


        # Loại đặt cọc
        self.label_deposit_type = tk.Label(self.frame_Date, text='Loại đặt cọc', font=font_text)
        self.label_deposit_type.grid(row=6, column=0)
        deposit_types = ['No Deposit', 'Refundable', 'Non Refund']
        self.deposit_type_value = tk.StringVar()
        self.deposit_type_combo = ttk.Combobox(self.frame_Date, textvariable=self.deposit_type_value, values=deposit_types,font=font_text, width=15,height=30)
        self.deposit_type_combo.grid(row=6, column=1)
        
        self.label_booking_changes = tk.Label(self.frame_Date, text='Số lần thay đổi', font=font_text)
        self.label_booking_changes.grid(row=7, column=0)
        self.entry_booking_changes = tk.Entry(self.frame_Date, font=font_text, width=15)
        self.entry_booking_changes.grid(row=7, column=1)
        self.booking_changes_value = tk.StringVar()
        self.entry_booking_changes.config(textvariable=self.booking_changes_value)
        
        self.label_days_in_waiting_list = tk.Label(self.frame_Date, text='Số ngày đợi', font=font_text)
        self.label_days_in_waiting_list.grid(row=8, column=0)
        self.entry_days_in_waiting_list = tk.Entry(self.frame_Date, font=font_text, width=15)
        self.entry_days_in_waiting_list.grid(row=8, column=1)
        self.days_in_waiting_list_value = tk.StringVar()
        self.entry_days_in_waiting_list.config(textvariable=self.days_in_waiting_list_value)
        
        self.label_reservation_status = tk.Label(self.frame_Date, text='Trạng thái cuối cùng', font=font_text)
        self.label_reservation_status.grid(row=9, column=0)
        reservation_statuss = ['Check-Out' ,'Canceled', 'No-Show']
        self.reservation_status_value = tk.StringVar()
        self.reservation_status_combo = ttk.Combobox(self.frame_Date, textvariable=self.reservation_status_value, values=reservation_statuss,font=font_text, width=15,height=30)
        self.reservation_status_combo.grid(row=9, column=1)


        # bảng dich vụ
        self.frame_Service = tk.Frame(self.frame)
        self.frame_Service.grid(row=0,column=2,sticky="n",padx=20)
        # dịch vụ đi kèm
        self.label_Service = tk.Label(self.frame_Service,text='Dịch vụ ', font= font_text)
        self.label_Service.grid(row=0,column=0,columnspan=2)
        
        self.label_meal = tk.Label(self.frame_Service, text='Bữa ăn', font=font_text)
        self.label_meal.grid(row=1, column=0)
        meals = ['BB', 'FB', 'HB', 'SC', 'Undefined']
        self.meal_value = tk.StringVar()
        self.meal_combo = ttk.Combobox(self.frame_Service, textvariable=self.meal_value, values=meals,font=font_text, width=15,height=30)
        self.meal_combo.grid(row=1, column=1)

        
        # Chỗ đỗ xe
        self.label_required_car_parking_spaces = tk.Label(self.frame_Service, text='Chỗ đỗ xe', font=font_text)
        self.label_required_car_parking_spaces.grid(row=2, column=0)
        car_parking_values = ['Có', 'Không']
        self.required_car_parking_spaces_value = tk.StringVar()
        self.car_parking_combo = ttk.Combobox(self.frame_Service, textvariable=self.required_car_parking_spaces_value, values=car_parking_values,font=font_text, width=14,height=30)
        self.car_parking_combo.grid(row=2, column=1)


        self.label_total_of_special_requests = tk.Label(self.frame_Service, text='Tổng số các dịch vụ', font=font_text)
        self.label_total_of_special_requests.grid(row=3, column=0)
        self.entry_total_of_special_requests = tk.Entry(self.frame_Service, font=font_text, width=15)
        self.entry_total_of_special_requests.grid(row=3, column=1)
        self.total_of_special_requests_value = tk.StringVar()
        self.entry_total_of_special_requests.config(textvariable=self.total_of_special_requests_value)
        
        # Nhà cung cấp
        self.label_distribution_channel = tk.Label(self.frame_Service, text='Kênh đặt chỗ', font=font_text)
        self.label_distribution_channel.grid(row=4, column=0)
        distribution_channel_values = ['Direct', 'Corporate', 'TA/TO', 'Undefined', 'GDS']
        self.distribution_channel_value = tk.StringVar()
        self.distribution_channel_combo = ttk.Combobox(self.frame_Service, textvariable=self.distribution_channel_value, values=distribution_channel_values,font= font_text, width=14,height=30)
        self.distribution_channel_combo.grid(row=4, column=1)

        


        
        
        self.frame_P = tk.Frame(self.root)
        self.frame_P.grid(row=2,column=0,columnspan=3)
        
        self.label_P = tk.Label(self.frame_P,text='Chọn thuộc tính dự đoán',font=font_text)
        self.label_P.grid(row=0,column=0, columnspan=2)
        self.label_hotel = tk.Label(self.frame_P, text='Loại phòng', font=font_text)
        self.label_hotel.grid(row=1, column=0)
        hotel_types = ['Resort Hotel', 'City Hotel']
        self.hotel_value = tk.StringVar()
        self.hotel_combo = ttk.Combobox(self.frame_P, textvariable=self.hotel_value, values=hotel_types,font=font_text, width=15,height=30)
        self.hotel_combo.grid(row=1, column=1)

        
        # Hủy phòng
        self.label_is_canceled = tk.Label(self.frame_P, text='Hủy phòng', font=font_text)
        self.label_is_canceled.grid(row=2, column=0)
        is_canceled_values = ['Có', 'Không']
        self.is_canceled_value = tk.StringVar()
        self.is_canceled_combo = ttk.Combobox(self.frame_P, textvariable=self.is_canceled_value, values=is_canceled_values,font=font_text, width=15,height=30)
        self.is_canceled_combo.grid(row=2, column=1)

        
        self.frame_Action = tk.Frame(self.root)
        self.frame_Action.grid(row=3,column=0,columnspan=3)
        
        self.label_Action = tk.Label(self.frame_Action, text='Dự đoán',font=font_header)
        self.label_Action.grid(row=0,column=0,columnspan=2)
        self.label_algorithm = tk.Label(self.frame_Action, text='Loại thuật toán', font=font_text)
        self.label_algorithm.grid(row=1, column=0)
        room_types = ['RandomForest', 'DecesionTree']
        self.algorithm_value = tk.StringVar()
        self.room_type_combo = ttk.Combobox(self.frame_Action, textvariable=self.algorithm_value, values=room_types,font=font_text, width=14, height =30)
        self.room_type_combo.grid(row=1, column=1)
        
        self.btn_Pre_Cancel = tk.Button(self.frame_Action,text='Dự đoán hủy phòng',font=font_text, command=self.predict_Cancel)
        self.btn_Pre_Cancel.grid(row=2,column=0,padx=10,pady=10)
        self.btn_Pre_Hotel = tk. Button(self.frame_Action,text='Dụ đoán loại phòng',font=font_text, command=self.predict_Hotel)
        self.btn_Pre_Hotel.grid(row=2,column=1)

        self.root.mainloop()
        
    def on_validate_input(P):
        if P == "" or P.isdigit():
            return True
        else:
            messagebox.showerror("Lỗi", "Vui lòng chỉ nhập số.")
            return False    
    def load(self):
        # Lấy thông tin từ các trường và combobox
        self.adults = self.adults_value.get()
        self.children = self.children_value.get()
        self.previous_cancellations = self.previous_cancellations_value.get()
        self.previous_bookings_not_canceled = self.previous_bookings_not_canceled_value.get()
        self.total_nights = self.TotalNights_value.get()
        self.adr = self.adr_value.get()
        self.days_in_waiting_list = self.days_in_waiting_list_value.get()
        self.booking_changes = self.booking_changes_value.get()
        self.total_of_special_requests = self.total_of_special_requests_value.get()
        
        bookingdate = self.BookingDate_value.get()
        bookingdate = datetime.strptime(bookingdate, "%m/%d/%y")
        arrival_date = self.arrival_date_value.get()
        arrival_date = datetime.strptime(arrival_date, "%m/%d/%y")
        # Tách giá trị năm, tháng và ngày
        self.arrival_date_year = arrival_date.year
        self.arrival_date_month = arrival_date.month
        self.arrival_date_day_of_month = arrival_date.day
        
        self.leadtime = arrival_date - bookingdate
        self.leadtime = self.leadtime.days
        self.is_repeated_guest = self.is_repeated_guest_value.get()
        self.required_car_parking_spaces = self.required_car_parking_spaces_value.get()
        self.is_canceled = self.is_canceled_value.get()
        yesno_mapping = {'Có':1,'Không':0}
        if self.is_repeated_guest in yesno_mapping:
            self.is_repeated_guest = yesno_mapping[self.is_repeated_guest]
        if self.required_car_parking_spaces in yesno_mapping:
            self.required_car_parking_spaces = yesno_mapping[self.required_car_parking_spaces]
        if self.is_canceled in yesno_mapping:
            self.is_canceled = yesno_mapping[self.is_canceled]
        
        self.country = self.country_value.get()
        country_mapping = {'Bồ Đào Nha': 0,
            'Vương quốc Anh': 1,
            'Hoa Kỳ': 2,
            'Tây Ban Nha': 3,
            'Ireland': 4,
            'Pháp': 5,
            'Không rõ': 6,
            'Romania': 7,
            'Na Uy': 8,
            'Oman': 9,
            'Argentina': 10,
            'Ba Lan': 11,
            'Đức': 12,
            'Bỉ': 13,
            'Thụy Sĩ': 14,
            'Trung Quốc': 15,
            'Hy Lạp': 16,
            'Ý': 17,
            'Hà Lan': 18,
            'Đan Mạch': 19,
            'Nga': 20,
            'Thụy Điển': 21,
            'Úc': 22,
            'Estonia': 23,
            'Cộng hòa Séc': 24,
            'Brasil': 25,
            'Phần Lan': 26,
            'Mozambique': 27,
            'Botswana': 28,
            'Luxembourg': 29,
            'Slovenia': 30,
            'Albania': 31,
            'Ấn Độ': 32,
            'Trung Quốc': 33,
            'Mexico': 34,
            'Maroc': 35,
            'Ukraina': 36,
            'San Marino': 37,
            'Latvia': 38,
            'Puerto Rico': 39,
            'Serbia': 40,
            'Chile': 41,
            'Áo': 42,
            'Belarus': 43,
            'Lithuania': 44,
            'Thổ Nhĩ Kỳ': 45,
            'Nam Phi': 46,
            'Angola': 47,
            'Israel': 48,
            'Quần đảo Cayman': 49,
            'Zambia': 50,
            'Cape Verde': 51,
            'Zimbabwe': 52,
            'Algeria': 53,
            'Hàn Quốc': 54,
            'Costa Rica': 55,
            'Hungary': 56,
            'Các Tiểu vương quốc Ả Rập Thống nhất': 57,
            'Tunisia': 58,
            'Jamaica': 59,
            'Croatia': 60,
            'Hồng Kông': 61,
            'Iran': 62,
            'Georgia': 63,
            'Andorra': 64,
            'Gibraltar': 65,
            'Uruguay': 66,
            'Jersey': 67,
            'Trung Phi': 68,
            'Cyprus': 69,
            'Colombia': 70,
            'Guernsey': 71,
            'Kuwait': 72,
            'Nigeria': 73,
            'Maldives': 74,
            'Venezuela': 75,
            'Slovakia': 76,
            'Fiji': 77,
            'Kazakhstan': 78,
            'Pakistan': 79,
            'Indonesia': 80,
            'Lebanon': 81,
            'Philippines': 82,
            'Senegal': 83,
            'Seychelles': 84,
            'Azerbaijan': 85,
            'Bahrain': 86,
            'New Zealand': 87,
            'Thailand': 88,
            'Dominican Republic': 89,
            'North Macedonia': 90,
            'Malaysia': 91,
            'Armenia': 92,
            'Nhật Bản': 93,
            'Sri Lanka': 94,
            'Cuba': 95,
            'Cameroon': 96,
            'Bosnia and Herzegovina': 97,
            'Mauritius': 98,
            'Comoros': 99,
            'Suriname': 100,
            'Uganda': 101,
            'Bulgaria': 102,
            'Ivory Coast': 103,
            'Jordan': 104,
            'Syria': 105,
            'Singapore': 106,
            'Burundi': 107,
            'Saudi Arabia': 108,
            'Việt Nam': 109,
            'Palau': 110,
            'Qatar': 111,
            'Egypt': 112,
            'Peru': 113,
            'Malta': 114,
            'Malawi': 115,
            'Ecuador': 116,
            'Madagascar': 117,
            'Iceland': 118,
            'Uzbekistan': 119,
            'Nepal': 120,
            'Bahamas': 121,
            'Macau': 122,
            'Togo': 123,
            'Taiwan': 124
        }
        if self.country in country_mapping:
            self.country = country_mapping[self.country]
            
        self.meal = self.meal_value.get()
        meal_mapping = {'BB': 0, 'FB': 1, 'HB': 2, 'SC': 3, 'Undefined': 4}
        if self.meal in meal_mapping:
            self.meal = meal_mapping[self.meal]
            
        self.reserved_room_type = self.reserved_room_type_value.get()
        self.deposit_type = self.deposit_type_value.get()
        self.reservation_status = self.reservation_status_value.get()
        self.customer_type = self.customer_type_value.get()
        self.distribution_channel = self.distribution_channel_value.get()
        self.hotel = self.hotel_value.get()
        
                # Ánh xạ cho distribution_channel
        distribution_channel_mapping = {
            'Direct': 1,
            'Corporate': 2,
            'TA/TO': 3,
            'Undefined': 4,
            'GDS': 5
        }
        # Ánh xạ cho reserved_room_type
        reserved_room_type_mapping = {
            'C': 1,
            'A': 2,
            'D': 3,
            'E': 4,
            'G': 5,
            'F': 6,
            'H': 7,
            'L': 8,
            'B': 9
        }
        # Ánh xạ cho deposit_type
        deposit_type_mapping = {
            'No Deposit': 1,
            'Refundable': 2,
            'Non Refund': 3
        }
        # Ánh xạ cho customer_type
        customer_type_mapping = {
            'Transient': 1,
            'Contract': 2,
            'Transient-Party': 3,
            'Group': 4
        }
        # Ánh xạ cho reservation_status
        reservation_status_mapping = {
            'Check-Out': 1,
            'Canceled': 2,
            'No-Show': 3
        }
        # Tạo bản đồ cho 'hotel'
        hotel_mapping = {
            'Resort Hotel': 1,
            'City Hotel': 2
        }
        
        if self.distribution_channel in distribution_channel_mapping:
            self.distribution_channel = distribution_channel_mapping[self.distribution_channel]
        if self.reserved_room_type in reserved_room_type_mapping:
            self.reserved_room_type = reserved_room_type_mapping[self.reserved_room_type]
        if self.deposit_type in deposit_type_mapping:
            self.deposit_type = deposit_type_mapping[self.deposit_type]
        if self.customer_type in customer_type_mapping:
            self.customer_type = customer_type_mapping[self.customer_type]
        if self.reservation_status in reservation_status_mapping:
            self.reservation_status = reservation_status_mapping[self.reservation_status]
        if self.hotel in hotel_mapping:
            self.hotel = hotel_mapping[self.hotel]
        
        self.algorithm = self.algorithm_value.get()

    def predict_Cancel (self):
        self.load()
        data = [[
            self.hotel,
            self.leadtime,
            self.arrival_date_month,
            self.arrival_date_year,
            self.arrival_date_day_of_month,
            self.adults,
            self.meal,
            self.country,
            self.distribution_channel,
            self.is_repeated_guest,
            self.previous_cancellations,
            self.previous_bookings_not_canceled,
            self.reserved_room_type,
            self.booking_changes,
            self.deposit_type,
            self.days_in_waiting_list,
            self.customer_type,
            self.adr,
            self.required_car_parking_spaces,
            self.total_of_special_requests,
            self.reservation_status,
            self.children,
            self.total_nights,
            ]]
        
        print(data)
        input_df = pd.DataFrame(data=data)
        if self.algorithm_value.get() == 'RandomForest':
            path = 'F:\Project\MachineLearning\HotelBooking\Model\Rd_clf.pkl'
        else:
            path = 'F:\Project\MachineLearning\HotelBooking\Model\Det_clf_hotel.pkl'
            
        with open(path, 'rb') as file:
            model = joblib.load(file)       
            # model = pickle.load('HotelBooking/Model/Rd_clf.pkl')
            dudoan = model.predict(input_df)
            confidence = model.predict_proba(input_df)
            print(dudoan)
            # In độ tự tin của các lớp
            for class_index, class_confidence in enumerate(confidence):
                print(f"Lớp {class_index}: {class_confidence}")
            if dudoan[0] == 1:
                messagebox.showinfo(self.algorithm_value.get(), "Khách hàng này có khả năng hủy phòng.")
                print('Có hủy')
            else:
                messagebox.showinfo(self.algorithm_value.get(), "Khách hàng này không hủy phòng.")
                print('Không hủy') 
    def predict_Hotel (self):
        self.load()
        data = [[
            self.hotel,
            self.leadtime,
            self.arrival_date_month,
            self.arrival_date_year,
            self.arrival_date_day_of_month,
            self.adults,
            self.meal,
            self.country,
            self.distribution_channel,
            self.is_repeated_guest,
            self.previous_cancellations,
            self.previous_bookings_not_canceled,
            self.reserved_room_type,
            self.booking_changes,
            self.deposit_type,
            self.days_in_waiting_list,
            self.customer_type,
            self.adr,
            self.required_car_parking_spaces,
            self.total_of_special_requests,
            self.reservation_status,
            self.children,
            self.total_nights,
            ]]
        
        print(data)
        input_df = pd.DataFrame(data=data)
        if self.algorithm_value.get() == 'RandomForest':
            path = 'F:\Project\MachineLearning\HotelBooking\Model\Rd_clf_hotel.pkl'
        else:
            path = 'F:\Project\MachineLearning\HotelBooking\Model\Det_clf_hotel.pkl'
            
        with open(path, 'rb') as file:
            model = joblib.load(file)       
            # model = pickle.load('HotelBooking/Model/Rd_clf.pkl')
            dudoan = model.predict(input_df)
            confidence = model.predict_proba(input_df)
            print(dudoan)
            # In độ tự tin của các lớp
            for class_index, class_confidence in enumerate(confidence):
                print(f"Lớp {class_index}: {class_confidence}")
            if dudoan[0] == 1:
                messagebox.showinfo(self.algorithm_value.get(), "Khách hàng này có khả năng chọn Resort Hotel.")
                print('Có hủy')
            else:
                messagebox.showinfo(self.algorithm_value.get(), "Khách hàng này có khả năng chọn City Hotel.")
                print('Không hủy') 
        
GiaoDien()