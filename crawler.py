import requests

url = (f'https://qavanin.ir/?CAPTION=&Zone=&IsTitleSearch=true&IsTitleSearch=false&IsTextSearch'
       '=false&_isLaw=false&_isRegulation=false&_IsVote=false&_isOpenion=false&SeachTextType=3'
       '&fromApproveDate=&APPROVEDATE=&IsTitleSubject=False&IsMain=&COMMANDNO=&fromCommandDate'
       '=&COMMANDDATE=&NEWSPAPERNO=&fromNewspaperDate=&NEWSPAPERDATE=&SortColumn=APPROVEDATE'
       '&SortDesc=True&Report_ID=&PageNumber=3&page={page_number}&size=25&txtZone=&txtSubjects=&txtExecutors'
       '=&txtApprovers=&txtLawStatus=&txtLawTypes=')

for number in range(1, 6):
    page_number = number
    url = url.format(page_number=page_number)
    res = requests.get(url)