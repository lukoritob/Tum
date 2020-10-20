from django.contrib import admin
from bmcs.models import UserProfile, VendorsTable, UpcomingTenders, BiddingStatusTable,  Bids

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(VendorsTable)
admin.site.register(UpcomingTenders)
admin.site.register(BiddingStatusTable)
admin.site.register(Bids)
#admin.site.register(BiddingTable)