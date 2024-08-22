import requests

for number in range(1, 6):

    # make 5 static https request for first 5 page for asked webpage

    page_number = number
    url = (f'https://qavanin.ir/?CAPTION=&Zone=&IsTitleSearch=true&IsTitleSearch=false&IsTextSearch'
           '=false&_isLaw=false&_isRegulation=false&_IsVote=false&_isOpenion=false&SeachTextType=3'
           '&fromApproveDate=&APPROVEDATE=&IsTitleSubject=False&IsMain=&COMMANDNO=&fromCommandDate'
           '=&COMMANDDATE=&NEWSPAPERNO=&fromNewspaperDate=&NEWSPAPERDATE=&SortColumn=APPROVEDATE'
           '&SortDesc=True&Report_ID=&PageNumber=3&page={page_number}&size=25&txtZone=&txtSubjects=&txtExecutors'
           '=&txtApprovers=&txtLawStatus=&txtLawTypes=')

    url = url.format(page_number=page_number)
    res = requests.get(url)
    print(res.status_code)