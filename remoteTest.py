#1. （A）請寫一個程式把裡面的字串反過來。
#   （B）請寫一個程式把裡面的字串，每個單字本身做反轉，但是單字的順序不變。
#舉例
#f ( "junyiacademy" ) == "ymedacaiynuj"
#f ( "flipped class room is important" ) == "deppilf ssalc moor si tnatropmi"

def testReverse(str):
    arr1=[]
    for i in str:
        arr1.append(i)
    arr1.reverse()
    result=''
    for i in arr1:
        result=result+i
    #print(result)
    return result
    
st1='junyiacademy'
testReverse(st1)
print(st1)

(2)
str2='flipped class room is important'
str2Split=str2.split(' ')
#str2Split

arr2=[]
for j in str2Split:
    str=testReverse(j)
    arr2.append(str)
    #print(str)
#print(arr2)
result=' '.join(arr2)
print(result)


#2. 請寫一個程式，Input 是一個數字，Output 是從 1 到這個數字，扣除掉所有 3 的
#倍數以及 5 的倍數，但是需要保留同時是 3 和 5 的倍數的總數字數。

#舉例
#Input：15
#所有的數字是：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
#其中 3, 6, 9, 12 被剔除；5, 10 被剔除；但是 15 被保留
#所以剩下來的數字是 1, 2, 4, 7, 8, 11, 13, 14, 15，因此
#Output：9

num=input('請填數字?')
#num
arr1=[]
for i in range(int(num)):
    oNum=i+1
    if(oNum%3!=0 and oNum%5!=0):
     arr1.append(oNum)   
    if(oNum%3==0 and oNum%5==0):
     arr1.append(oNum) 
print(len(arr1))

#3. 房間裡有三個袋子，一個只裝鉛筆，一個只裝原子筆，第三個有鉛筆也有原子筆。
#袋子是不透明的，單從袋子的外表上看不出任何差異，你不知道哪個袋子裝什麼。
#除了袋子上各貼了一個標示（"鉛筆"、"原子筆"、"混和"），且標示都是錯的
#（e.g. 標示鉛筆的袋子可能是混和的或是只裝原子筆）。
#你只能選一個袋子，拿出裡面一支筆，看是鉛筆還是原子筆，然後你要推論出這三
#個袋子分別的情況。請列出你的作法，以及解釋為什麼這樣可以找到答案。


###Ans: 
#(標籤B or C) A鉛筆:a1,a2...
#(標籤A or C) B原子筆:b1,b2...
#(標籤A or B) C混合:a11,b11...
#     if(標籤A){
#         if(取出鉛筆){
#            return 實際拿到C混合;
#         }else{
#            return 實際拿到C混合 or B原子筆;
#         } 
#     }else if(標籤B){
#         if(取出原子筆){
#            return 實際拿到C混合;
#         }else{
#            return 實際拿到C混合 or A鉛筆;
#         } 
#     }else if(標籤C){
#           if(取出原子筆){
#            return 實際拿到B原子筆;
#         }else{
#            return 實際拿到A鉛筆;
#         }
#     }
    
#4. 有三個人一起到迪士尼遊玩，中午肚子餓了，去餐廳點了一份現在最夯的冰雪奇緣
#雙人組，要價 900 元，付錢後，服務生發現今天套餐大特價，只要 750 元，因此
#服務生應該退還 150 元給這三個人，但是這位服務生一時鬼迷心竅，決定暗槓 60
#元，只退了 90 元給這三個遊客。
#那麼：三人各出 300 元 - 服務生還給他們一人 30 元 = 三人各出 270 元。270
#元 × 3 人+ 服務生私吞的 60 元 = 810 + 60 = 870 !? 怎麼不是 900 元呢？還
#有 30 元去哪了呢？請用敘述的方式，儘量清楚解釋問題出在哪裡。

###Ans: (1)用減法= 300 -30 =270 ; 但他們原本應該只要付250 所以是服務生藏的60需要在平分3分為20
#所以 270-20 =250 為來應付的價錢 (也是900-90=810 需要再減掉60才會是750 )
#(2)用加法算= 750 +90(退回的) =840 ; 840+60(還在服務生身上的) =900 

