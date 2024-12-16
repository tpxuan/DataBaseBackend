# api/urls.py
from django.urls import path
from .views import AdminLoginAPI, AdminCreateDiscussAPI, AdminCreatePostAPI, AdminGetMyDiscussAPI, AdminGetGoodsAPI, AdminDeleteGoodAPI, AdminSearchGoodAPI, AdminGetSellersAPI, AdminSearchSellerAPI, AdminGetSellerGoodsAPI, BuyerLoginAPI, BuyerModifyAPI, BuyerGetHistoryAPI, BuyerCreateDiscussAPI, BuyerCreatePostAPI, BuyerGetMyDiscussAPI, BuyerCreateCommentAPI, BuyerAllocAccountAPI, BuyerRegisterAPI, BuyerCreateOrderAPI, GetGoodDetailAPI, GetDetailCommentAPI, GetDiscussListAPI, SearchDiscussAPI, GetDiscussAPI, DeleteDiscussAPI, GetPostListAPI, DeletePostAPI, DeleteCommentAPI,  SellerLoginAPI, SellerModifyAPI, SellerCreateDiscussAPI, SellerCreatePostAPI, SellerGetMyDiscussAPI, SellerAllocAccountAPI, SellerRegisterAPI, SellerDeleteGoodAPI, SellerGetSellerGoodsAPI, SellerCreateGoods

urlpatterns = [
    path('adminlogin/', AdminLoginAPI.as_view(), name='admin-login'),
    path('AdminCreateDiscuss/', AdminCreateDiscussAPI.as_view(), name='admin-create-discuss'),
    path('AdminCreatePost/', AdminCreatePostAPI.as_view(), name='admin-create-post'),
    path('AdminGetMyDiscuss/', AdminGetMyDiscussAPI.as_view(), name='admin-get-my-discuss'),
    path('AdminGetGoods/', AdminGetGoodsAPI.as_view(), name='admin-get-goods'),
    path('AdminDeleteGood/', AdminDeleteGoodAPI.as_view(), name='admin-delete-good'),
    path('AdminSearchGood/', AdminSearchGoodAPI.as_view(), name='admin-search-good'),
    path('AdminGetSellers/', AdminGetSellersAPI.as_view(), name='admin-get-sellers'),
    path('AdminSearchSeller/', AdminSearchSellerAPI.as_view(), name='admin-search-seller'),
    path('AdminGetSellerGoods/', AdminGetSellerGoodsAPI.as_view(), name='admin-get-seller-goods'),
    path('BuyerLogin/', BuyerLoginAPI.as_view(), name='buyer-login'),
    path('BuyerModify/', BuyerModifyAPI.as_view(), name='buyer-modify'),
    path('BuyerGetHistory/', BuyerGetHistoryAPI.as_view(), name='buyer-get-history'),
    path('BuyerCreateDiscuss/', BuyerCreateDiscussAPI.as_view(), name='buyer-create-discuss'),
    path('BuyerCreatePost/', BuyerCreatePostAPI.as_view(), name='buyer-create-post'),
    path('BuyerGetMyDiscuss/', BuyerGetMyDiscussAPI.as_view(), name='buyer-get-my-discuss'),
    path('BuyerCreateComment/', BuyerCreateCommentAPI.as_view(), name='buyer-create-comment'),
    path('BuyerAllocAccount/', BuyerAllocAccountAPI.as_view(), name='buyer_alloc_account'),
    path('BuyerRegister/', BuyerRegisterAPI.as_view(), name='buyer-register'),
    path('BuyerCreateOrder/', BuyerCreateOrderAPI.as_view(), name='buyer-create-order'),
    path('GetGoodDetail/', GetGoodDetailAPI.as_view(), name='get-good-detail'),
    path('GetDetailComment/', GetDetailCommentAPI.as_view(), name='get-detail-comment'),
    path('GetDiscussList/', GetDiscussListAPI.as_view(), name='get-discuss-list'),
    path('SearchDiscuss/', SearchDiscussAPI.as_view(), name='search-discuss'),
    path('GetDiscuss/', GetDiscussAPI.as_view(), name='get-discuss'),
    path('DeleteDiscuss/', DeleteDiscussAPI.as_view(), name='delete-discuss'),
    path('GetPostList/', GetPostListAPI.as_view(), name='get-post-list'),
    path('DeletePost/', DeletePostAPI.as_view(), name='delete-post'),
    path('DeleteComment/', DeleteCommentAPI.as_view(), name='delete-comment'),
    path('SellerLogin/', SellerLoginAPI.as_view(), name='seller-login'),
    path('SellerModify/', SellerModifyAPI.as_view(), name='seller-modify'),
    path('SellerCreateDiscuss/', SellerCreateDiscussAPI.as_view(), name='seller-create-discuss'),
    path('SellerCreatePost/', SellerCreatePostAPI.as_view(), name='seller-create-post'),
    path('SellerGetMyDiscuss/', SellerGetMyDiscussAPI.as_view(), name='seller-get-my-discuss'),
    path('SellerAllocAccount/', SellerAllocAccountAPI.as_view(), name='seller-alloc-account'),
    path('SellerRegister/', SellerRegisterAPI.as_view(), name='seller-register'),
    path('SellerDeleteGood/', SellerDeleteGoodAPI.as_view(), name='seller-delete-good'),
    path('SellerGetSellerGoods/', SellerGetSellerGoodsAPI.as_view(), name='seller-get-seller-goods'),
    path('SellerCreateGoods/', SellerCreateGoods.as_view(), name='seller-create-goods'),
]


print(urlpatterns)