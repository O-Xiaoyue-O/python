while True:
    id_number=input('請輸入身分證字號,若不想繼續請輸入exit:')#使用者輸入身分證
    if id_number=='exit':
        break
    else:
        city={'A':'台北市','B':'台中市','C':'基隆市','D':'台南市','E':'高雄市','F':'台北縣','G':'宜蘭縣','H':'宜蘭縣',
        'I':'嘉義市','J':'新竹縣','K':'苗栗縣','L':'台中縣','M':'南投縣','N':'彰化縣','O':'新竹市','P':'雲林縣','Q':'嘉義縣',
        'R':'台南縣','S':'高雄縣','T':'屏東縣','U':'花蓮縣','V':'台東縣','W':'金門縣','X':'澎湖縣','Y':'陽明山','Z':'連江縣'}#python字典
        
        while True:#用來測試使用者輸入是否正確,若正確則跳脫迴圈
            try:
                test_id=city[id_number[0:1]]#用來測試第一個字母是否正確
            except KeyError:#如果執行try裡面字典查不到(回傳KeyError),請使用者重新輸入
                id_number=input('錯誤,請確認是否輸入為身份證字號(注意大寫),並重新輸入:')
                continue#強制進行下一次迴圈
            if len(id_number)==10 and id_number[1:11].isdigit()==True:#第一個是檢測是否為10個字母,第二個則是檢測第2~10是否為數字
                if int(id_number[1:2])==1:#檢查第2個字串並輸出男女生,注意要轉成int,否則是字串VS數字
                    print('你是男生')
                    break
                elif int(id_number[1:2])==2:
                    print('妳是女生')
                    break
                else:#如果不是1或2則重新輸入一次
                    id_number=input('錯誤,請確認是否輸入為身份證字號,並重新輸入:')
            else:
                id_number=input('錯誤,請確認是否輸入為身份證字號(長度應為10碼),並重新輸入:')

        print('出生於'+city[id_number[0:1]]+'\n')#查詢字典(city)並輸出出生的城市
