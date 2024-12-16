# api/views.py
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Admin, Buyer, Good, Discuss, Order, Post, Comment, Seller

DISCUSS_ID = 10000000
POST_ID = 10000000
COMMENT_ID = 10000000
ACCOUNT = 10000000
GOOD_ID = 10000000
ORDER_ID = 10000000

class AdminLoginAPI(APIView):
    def post(self, request):
        account = request.data.get('account')
        password = request.data.get('password')
        try:
            admin = Admin.objects.get(account=account, password=password)
            response_data = {
                'result': {
                    'account': account,
                    'password': password,
                    'nickname': admin.nickname,
                    'sex': admin.sex,
                    'birthday': admin.birthday,
                    'desc': admin.desc
                }
            }
            return JsonResponse(response_data)
        except Admin.DoesNotExist:
            response_data = {
                'result': {
                    'account': account,
                    'password': password,
                    'nickname': "",
                    'sex': "",
                    'birthday': "",
                    'desc': ""
                }
            }
            return JsonResponse(response_data)

class AdminCreateDiscussAPI(APIView):
    def post(self, request):
        account = request.data.get('account')
        date = request.data.get('date')
        title = request.data.get('title')
        content = request.data.get('content')
        discuss = Discuss.objects.create(disscussId = DISCUSS_ID,
                                         discussTitle = title,discussTime = date,
                                         discussContent = content,
                                         discussBy = account,
                                         discussByType = "管理员")
        discuss.save()
        DISCUSS_ID += 1
        return JsonResponse({'success': True})

class AdminCreatePostAPI(APIView):
    def post(self, request):
        account = request.data.get('account')
        date = request.data.get('date')
        content = request.data.get('postContent')
        discussID = request.data.get('discussID')
        post = Post.objects.create(postId = POST_ID,
                                   postContent = content,
                                   postTime = date,
                                   postBy = account,
                                   postByType = "管理员",
                                   postByDiscussId = discussID)
        post.save()
        POST_ID += 1
        return JsonResponse({'success': True})

class AdminGetMyDiscussAPI(APIView):
    def get(self, request):
        account = request.query_params.get('account')
        discuss = Discuss.objects.filter(discussBy=account)
        data = []
        for i in discuss:
            discussByName = ""
            if i.discussByType == "管理员":
                discussByName = Admin.objects.get(account=i.discussBy).nickname
            elif i.discussByType == "消费者":
                discussByName = Buyer.objects.get(account=i.discussBy).nickname
            else:
                discussByName = Seller.objects.get(account=i.discussBy).nickname
            data.append({
                'DiscussID': i.discussId,
                'DiscussTitle': i.discussTitle,
                'DiscussTime': i.discussTime,
                'DiscussBy': discussByName,
                'DiscussByType': i.discussByType
            })
        return JsonResponse({'data': data})

class AdminGetGoodsAPI(APIView):
    def get(self, request):
        goods = Good.objects.all()
        data = []
        for i in goods:
            data.append({
                'goodName': i.goodName,
                'goodBySellerId':i.goodBySellerId,
                'goodId': i.goodID,
                'goodPic':i.goodPic,
            })
        return JsonResponse({'data': data})
    
class AdminDeleteGoodAPI(APIView):
    def get(self, request):
        goodId = request.query_params.get('id')
        try:
            good = Good.objects.get(goodId=goodId)
            good.delete()
            return JsonResponse({'success': True})
        except Good.DoesNotExist:
            return JsonResponse({'error': 'Good not found'}, status=status.HTTP_404_NOT_FOUND)
        
class AdminSearchGoodAPI(APIView):
    def get(self, request):
        keyword = request.query_params.get('name')
        goods = Good.objects.filter(goodName__icontains=keyword)
        data = []
        for i in goods:
            data.append({
                'goodName': i.goodName,
                'goodBySellerId':i.goodBySellerId,
                'goodId': i.goodID,
                'goodPic':i.goodPic,
            })
        return JsonResponse({'data': data})
    
class AdminGetSellersAPI(APIView):
    def get(self, request):
        seller = Seller.objects.all()
        data = []
        for i in seller:
            data.append({
                'sellerName': i.nickname,
                'sellerId': i.account,
            })
        return JsonResponse({'data': data})

class AdminSearchSellerAPI(APIView):
    def get(self, request):
        name = request.query_params.get('name')
        seller = Seller.objects.filter(nickname__icontains=name)
        data = []
        for i in seller:
            data.append({
                'sellerName': i.nickname,
                'sellerId': i.account,
            })
        return JsonResponse({'data': data})
    
class AdminGetSellerGoodsAPI(APIView):
    def get(self, request):
        id = request.query_params.get('id')
        goods = Good.objects.filter(goodBySellerID=id)
        data = []
        for i in goods:
            data.append({
                'goodId': i.goodId,
                'goodName': i.goodName,
                'goodPic': i.goodPic,
            })
        return JsonResponse({'data': data})
    
class BuyerLoginAPI(APIView):
    def post(self, request):
        account = request.data.get('account')
        password = request.data.get('password')
        try:
            buyer = Buyer.objects.get(account=account, password=password)
            response_data = {
                'result': {
                    'account': account,
                    'password': password,
                    'nickname': buyer.nickname,
                    'sex': buyer.sex,
                    'birthday': buyer.birthday,
                    'desc': buyer.desc
                }
            }
            return JsonResponse(response_data)
        except Buyer.DoesNotExist:
            response_data = {
                'result': {
                    'account': account,
                    'password': password,
                    'nickname': "",
                    'sex': "",
                    'birthday': "",
                    'desc': ""
                }
            }
            return JsonResponse(response_data)
        
class BuyerModifyAPI(APIView):
    def post(self, request):
        account = request.data.get('account')
        password = request.data.get('password')
        nickname = request.data.get('nickname')
        sex = request.data.get('sex')
        birthday = request.data.get('birthday')
        desc = request.data.get('desc')
        buyer = Buyer.objects.get(account=account)
        buyer.password = password
        buyer.nickname = nickname
        buyer.sex = sex
        buyer.birthday = birthday
        buyer.desc = desc
        buyer.save()
        return JsonResponse({'success': True})
    
class BuyerGetHistoryAPI(APIView):
    def get(self, request):
        account = request.data.get('account')
        orders = Order.objects.filter(orderBy=account)
        data = []
        for i in orders:
            data.append({'orderName': i.orderName,
                         'orderId': i.orderId,
                         'orderNum': i.orderNum,
                         'orderPrice': i.orderPrice,
                         'orderDate':i.orderDate,
                         'orderGoodId':i.orderGoodId,
                         'orderPos':i.orderPos})
        return JsonResponse({'data': data})
    
class BuyerCreateDiscussAPI(APIView):
    def post(self, request):
        account = request.data.get('account')
        date = request.data.get('date')
        title = request.data.get('title')
        content = request.data.get('content')
        discuss = Discuss.objects.create(disscussId = DISCUSS_ID,
                                         discussTitle = title,
                                         discussTime = date,
                                         discussContent = content,
                                         discussBy = account,
                                         discussByType = "消费者")
        discuss.save()
        DISCUSS_ID += 1
        return JsonResponse({'success': True})

class BuyerCreatePostAPI(APIView):
    def post(self, request):
        account = request.data.get('account')
        date = request.data.get('date')
        content = request.data.get('postContent')
        discussID = request.data.get('discussID')
        post = Post.objects.create(postId = POST_ID,
                                   postContent = content,
                                   postTime = date,
                                   postBy = account,
                                   postByType = "消费者",
                                   postByDiscussId = discussID)
        post.save()
        POST_ID += 1
        return JsonResponse({'success': True})
    
class BuyerGetMyDiscussAPI(APIView):
    def get(self, request):
        account = request.query_params.get('account')
        discuss = Discuss.objects.filter(discussBy=account)
        data = []
        for i in discuss:
            discussByName = ""
            if i.discussByType == "管理员":
                discussByName = Admin.objects.get(account=i.discussBy).nickname
            elif i.discussByType == "消费者":
                discussByName = Buyer.objects.get(account=i.discussBy).nickname
            else:
                discussByName = Seller.objects.get(account=i.discussBy).nickname
            data.append({
                'DiscussID': i.discussId,
                'DiscussTitle': i.discussTitle,
                'DiscussTime': i.discussTime,
                'DiscussBy': discussByName,
                'DiscussByType': i.discussByType
            })
        return JsonResponse({'data': data})
    
class BuyerCreateCommentAPI(APIView):
    def post(self, request):
        account = request.POST['account']
        date = request.POST['date']
        content = request.POST['content']
        score = request.POST['score']
        goodId = request.POST['goodId']
        comment = Comment(
            commentId=COMMENT_ID,
            commentById=account,
            commentTime=date,
            commentContent=content,
            commentScore=score,
            goodId=goodId
        )            
        comment.save()
        COMMENT_ID += 1
        return JsonResponse({'success': True})

class BuyerAllocAccountAPI(APIView):
    def get(self, request):
        global ACCOUNT
        buyerId = str(ACCOUNT)
        ACCOUNT += 1
        print(buyerId)
        return JsonResponse({'result': buyerId})
        
class BuyerRegisterAPI(APIView):
    def post(self, request):
        account = request.data.get('account')
        password = request.data.get('password')
        nickname = request.data.get('nickname')
        sex = request.data.get('sex')
        birthday = request.data.get('birthday')
        desc = request.data.get('desc')
        buyer = Buyer(
            account=account,
            password=password,
            nickname=nickname,
            sex=sex,
            birthday=birthday,
            desc=desc
        )
        buyer.save()
        return JsonResponse({'success': True})
    
class BuyerCreateOrderAPI(APIView):
    def post(self, request):
        orderBy = request.data.get('account')
        orderGoodId = request.data.get('orderGoodId')
        orderDate = request.data.get('orderDate')
        orderNum = request.data.get('orderNum')
        orderPrice = request.data.get('orderPrice')
        orderPos = request.data.get('orderPos')
        good = Good.objects.get(goodId=orderGoodId)
        orderName = good.goodName
        order = Order(orderBy=orderBy,
                      orderGoodId=orderGoodId,
                      orderDate=orderDate,
                      orderNum=orderNum,
                      orderPrice=orderPrice,
                      orderPos=orderPos,
                      orderName=orderName,orderId = ORDER_ID)
        order.save()
        ORDER_ID += 1
        return JsonResponse({'success': True})

class SellerLoginAPI(APIView):
    def post(self, request):
        account = request.data.get('account')
        password = request.data.get('password')
        try:
            seller = Seller.objects.get(account=account, password=password)
            response_data = {
                'result': {
                    'account': account,
                    'password': password,
                    'nickname': seller.nickname,
                    'sex': seller.sex,
                    'birthday': seller.birthday,
                    'desc': seller.desc
                }
            }
            return JsonResponse(response_data)
        except Seller.DoesNotExist:
            response_data = {
                'result': {
                    'account': account,
                    'password': password,
                    'nickname': "",
                    'sex': "",
                    'birthday': "",
                    'desc': ""
                }
            }
            return JsonResponse(response_data)
        
class SellerModifyAPI(APIView):
    def post(self, request):
        account = request.data.get('account')
        password = request.data.get('password')
        nickname = request.data.get('nickname')
        sex = request.data.get('sex')
        birthday = request.data.get('birthday')
        desc = request.data.get('desc')
        seller = Seller.objects.get(account=account)
        seller.password = password
        seller.nickname = nickname
        seller.sex = sex
        seller.birthday = birthday
        seller.desc = desc
        seller.save()
        return JsonResponse({'success': True})
    
class SellerCreateDiscussAPI(APIView):
    def post(self, request):
        account = request.data.get('account')
        date = request.data.get('date')
        title = request.data.get('title')
        content = request.data.get('content')
        discuss = Discuss.objects.create(disscussId = DISCUSS_ID,
                                         discussTitle = title,
                                         discussTime = date,
                                         discussContent = content,
                                         discussBy = account,
                                         discussByType = "商家")
        discuss.save()
        DISCUSS_ID += 1
        return JsonResponse({'success': True})
    
class SellerCreatePostAPI(APIView):
    def post(self, request):
        account = request.data.get('account')
        date = request.data.get('date')
        content = request.data.get('postContent')
        discussID = request.data.get('discussID')
        post = Post.objects.create(postId = POST_ID,
                                   postContent = content,
                                   postTime = date,
                                   postBy = account,
                                   postByType = "商家",
                                   postByDiscussId = discussID)
        post.save()
        POST_ID += 1
        return JsonResponse({'success': True})
    
class SellerGetMyDiscussAPI(APIView):
    def get(self, request):
        account = request.query_params.get('account')
        discuss = Discuss.objects.filter(discussBy=account)
        data = []
        for i in discuss:
            discussByName = ""
            if i.discussByType == "管理员":
                discussByName = Admin.objects.get(account=i.discussBy).nickname
            elif i.discussByType == "消费者":
                discussByName = Buyer.objects.get(account=i.discussBy).nickname
            else:
                discussByName = Seller.objects.get(account=i.discussBy).nickname
            data.append({
                'DiscussID': i.discussId,
                'DiscussTitle': i.discussTitle,
                'DiscussTime': i.discussTime,
                'DiscussBy': discussByName,
                'DiscussByType': i.discussByType
            })
        return JsonResponse({'data': data})
    
class SellerAllocAccountAPI(APIView):
    def post(self, request):
        sellerId = ACCOUNT
        ACCOUNT += 1
        return JsonResponse({'result': sellerId})
    
class SellerRegisterAPI(APIView):
    def post(self, request):
        account = request.data.get('account')
        password = request.data.get('password')
        nickname = request.data.get('nickname')
        sex = request.data.get('sex')
        birthday = request.data.get('birthday')
        desc = request.data.get('desc')
        seller = Seller(
            account=account,
            password=password,
            nickname=nickname,
            sex=sex,
            birthday=birthday,
            desc=desc
        )
        seller.save()
        return JsonResponse({'success': True})

class SellerDeleteGoodAPI(APIView):
    def get(self, request):
        goodId = request.query_params.get('id')
        try:
            good = Good.objects.get(goodId=goodId)
            good.delete()
            return JsonResponse({'success': True})
        except Good.DoesNotExist:
            return JsonResponse({'error': 'Good not found'}, status=status.HTTP_404_NOT_FOUND)
        
class SellerGetSellerGoodsAPI(APIView):
    def get(self, request):
        sellerId = request.query_params.get('id')
        goods = Good.objects.filter(goodBySellerId=sellerId)
        data = []
        for i in goods:
            data.append({
                'goodName': i.goodName,
                'goodId': i.goodID,
                'goodPic':i.goodPic,
            })
        return JsonResponse({'data': data})
    
class SellerCreateGoods(APIView):
    def post(self, request):
        data = request.data
        goods = Good.objects.create(
            goodId=GOOD_ID,
            goodBySellerId=data['account'],
            goodName=data['goodName'],
            goodPrice=data['goodPrice'],
            goodPromotion=data['goodPromotion'],
            goodServe=data['goodServe'],
            goodPic=data['goodPic']
        )
        GOOD_ID += 1
        goods.save()
        return JsonResponse({'success': True})

class GetGoodDetailAPI(APIView):
    def get(self, request):
        goodId = request.GET.get('id')
        good = Good.objects.get(goodId=goodId)
        orders = Order.objects.filter(orderGoodId=goodId)
        comments = Comment.objects.filter(goodId=goodId)
        scoreSum = 0
        for comment in comments:
            scoreSum += comment.CommentScore
        seller = Seller.objects.get(account=good.goodBySellerId)
        response_data = {
                'result': {
                    'goodName': good.goodName,
                    'goodPic': good.goodPic,
                    'goodSellNum': orders.count(),
                    'goodCommentNum': comments.count(),
                    'goodScore': scoreSum / comments.count(),
                    'goodSeller': seller.nickname,
                    'goodPrice': good.goodPrice,
                    'goodPromotion': good.goodPromotion,
                    'goodServe': good.goodServe,
                    'goodDesc': good.desc
                }
            }
        return JsonResponse(response_data)

class GetDetailCommentAPI(APIView):
    def get(self, request):
        goodId = request.GET.get('id')
        commentList = Comment.objects.filter(goodId=goodId)
        data = []
        for i in commentList:
            buyer = Buyer.objects.get(account=i.commentById)
            data.append({
                'commentId': i.commentId,
                'commentByName': buyer.nickname,
                'commentById':i.commentById,
                'CommentTime':i.commentTime,
                'CommentContent':i.commentContent,
                'CommentScore':i.commentScore
            })
        return JsonResponse({'data': data})

class GetDiscussListAPI(APIView):
    def get(self, request):
        discussList = Discuss.objects.all()
        data = []
        for i in discussList:
            discussByName = ""
            if i.discussByType == "管理员":
                discussByName = Admin.objects.get(account=i.discussBy).nickname
            elif i.discussByType == "消费者":
                discussByName = Buyer.objects.get(account=i.discussBy).nickname
            else:
                discussByName = Seller.objects.get(account=i.discussBy).nickname
            data.append({
                'DiscussId': i.discussId,
                'DiscussTitle': i.discussTitle,
                'DiscussTime': i.discussTime,
                'DiscussBy': discussByName,
                'DiscussByType': i.discussByType,
            })
        return JsonResponse({'data': data})

class SearchDiscussAPI(APIView):
    def get(self, request):
        keyword = request.GET.get('name')
        discussList = Discuss.objects.filter(discussTitle__icontains=keyword)
        data = []
        for i in discussList:
            discussByName = ""
            if i.discussByType == "管理员":
                discussByName = Admin.objects.get(account=i.discussBy).nickname
            elif i.discussByType == "消费者":
                discussByName = Buyer.objects.get(account=i.discussBy).nickname
            else:
                discussByName = Seller.objects.get(account=i.discussBy).nickname
            data.append({
                'DiscussId': i.discussId,
                'DiscussTitle': i.discussTitle,
                'DiscussTime': i.discussTime,
                'DiscussBy': discussByName,
                'DiscussByType': i.discussByType,
            })
        return JsonResponse({'data': data})

class GetDiscussAPI(APIView):
    def get(self, request):
        discussId = request.GET.get('id')
        discuss = Discuss.objects.get(discussId=discussId)
        discussByName = ""
        if discuss.discussByType == "管理员":
            discussByName = Admin.objects.get(account=discuss.discussBy).nickname
        elif discuss.discussByType == "消费者":
            discussByName = Buyer.objects.get(account=discuss.discussBy).nickname
        else:
            discussByName = Seller.objects.get(account=discuss.discussBy).nickname
        response_data = {
                'result': {
                    'DiscussById': discuss.discussBy,
                    'DiscussTitle': discuss.discussTitle,
                    'DiscussTime': discuss.discussTime,
                    'DiscussByName': discussByName,
                    'DiscussByType': discuss.discussByType,
                    'DiscussContent': discuss.discussContent
                }
            }
        return JsonResponse(response_data)
    
class DeleteDiscussAPI(APIView):
    def post(self, request):
        discussId = request.query_parms.get('id')
        discuss = Discuss.objects.get(discussId=discussId)
        discuss.delete()
        return JsonResponse({'success': True})

class GetPostListAPI(APIView):
    def get(self, request):
        discussId = request.query_parms.get('id')
        postList = Post.objects.filter(postByDiscussId=discussId)
        data = []
        for i in postList:
            postByName = ""
            if i.postByType == "管理员":
                postByName = Admin.objects.get(account=i.postBy).nickname
            elif i.postByType == "消费者":
                postByName = Buyer.objects.get(account=i.postBy).nickname
            else:
                postByName = Seller.objects.get(account=i.postBy).nickname
            data.append({
                'postId': i.postId,
                'postById': i.postBy,
                'postByName': postByName,
                'postByType': i.postByType,
                'postContent': i.postContent,
                'postTime': i.postTime
            })
        return JsonResponse({'data': data})
    
class DeletePostAPI(APIView):
    def post(self, request):
        postId = request.query_parms.get('id')
        post = Post.objects.get(postId=postId)
        post.delete()
        return JsonResponse({'success': True})
    
class DeleteCommentAPI(APIView):
    def post(self, request):
        commentId = request.query_parms.get('id')
        comment = Comment.objects.get(commentId=commentId)
        comment.delete()
        return JsonResponse({'success': True})
