#!/usr/bin/env python
# coding: utf-8

# In[39]:


def estimateRepairsFlip (squarefeet, bigTicketItems):
    interiorBudget = (squarefeet * 20) * 1.05
    exteriorBudget = (3500 * bigTicketItems) * 1.1
    repairCost = interiorBudget + exteriorBudget
    print("For a house with " + str(squarefeet) + " square feet and " + str(bigTicketItems) + " big ticket items")
    print("The rough estimated repair would be " + str(repairCost))


estimateRepairsFlip (1500, 3)


# In[38]:


def estimateRepairsRental(squarefeet, bigTicketItems):
    interiorBudget = (squarefeet * 11) * 1.02
    exteriorBudget = (3500 * bigTicketItems) * 1.1
    repairCost = interiorBudget + exteriorBudget
    print("For a house with " + str(squarefeet) + " square feet and " + str(bigTicketItems) + " big ticket items")
    print("The rough estimated repair would be " + str(repairCost))

    
estimateRepairsRental (1500, 3)


# In[127]:


def maxAllowableOfferFlip(wholeSaleMargin, arv, estimateRepairs, arvDiscount,):
    maxOffer = ((arv * arvDiscount) - estimateRepairs) - wholeSaleMargin
    print ("The max offer that should be made on this house is " + str(maxOffer) + " .")


maxAllowableOfferFlip(6500, 330000, 43000, .80,)   


# In[126]:


def maxAllowableOfferSameDayClose(wholeSaleMargin, arv, estimateRepairs, arvDiscount,):
    maxOffer = (((arv * arvDiscount) - estimateRepairs) - wholeSaleMargin) *.96
    print ("The max offer that should be made on this house is " + str(maxOffer) + " .")

    
maxAllowableOfferSameDayClose(6500, 330000, 43000, .80)


# In[80]:


def capRateByPrice( monthRent, homePrice, estimateRepairsRental, expense = .7):
    totalCost = estimateRepairsRental + homePrice
    cap = ((monthRent * 12) * expense)
    rate = (cap / totalCost) * 100
    print("The cap-rate for this property is " + str(rate))
    
    
capRateByPrice (1200, 180000, 0)


# In[67]:


def capRateByPercent(monthRent, capRate = .06, expense = .7):
    Offer = ((monthRent * 12) * expense) / capRate
    print("For a 6 percent cap-rate, you should offer no more than " + str(Offer) + ".")


capRateByPercent (1200)


# In[68]:


def maxAllowableOfferRental(wholeSaleMargin, monthRent, estimateRepairsRental, capRate = .06, expense = .7):
    maxOffer = ((monthRent * 12) * expense) / capRate - (wholeSaleMargin + estimateRepairsRental)
    print("For a 6 percent cap rate, you should offer no more than " + str(maxOffer) + ".")
    
    
maxAllowableOfferRental (5000, 1200, 32320)


# In[116]:


def monthlyMortgagePayment(purchasePrice, percentDownPayment, interest, years):
    downPayment = percentDownPayment / 100
    principle = purchasePrice - (purchasePrice * downPayment)
    interest = interest / 100
    nper = years * 12
    interestMonthly = interest / 12
    numerator = interestMonthly * ((1 + interestMonthly)**nper)
    denominator = (1 + interestMonthly)**nper-1
    
    monthlyPayment = float("{0: .2f}".format(principle * numerator / denominator))
    print(monthlyPayment)
    
    
monthlyMortgagePayment (184000, 25, 4, 30)


# In[124]:


def rentalCashFlow(purchasePrice, percentDownPayment, rent, monthlyMortgage, taxes, hoa, insurance, management = .1, vacancyRate = .08):
    vacancyRent = rent - (rent * vacancyRate)
    managementRent = vacancyRent - (rent * management)
    cashFlow = managementRent - monthlyMortgage - taxes - hoa - insurance
    yearCashFlow = cashFlow * 12
    downPayment = percentDownPayment / 100
    investedCash = purchasePrice * downPayment
    formattedCashFlow = "{:.2f}".format(cashFlow)
    formattedYearCashFlow = "{:.2f}".format(yearCashFlow)
    cashOnCashReturn = (yearCashFlow / investedCash) * 100
    formattedCashOnCashReturn = "{:.5f}".format(cashOnCashReturn)
    print ("The monthly cash flow for this property is "+ str(formattedCashFlow) + ".")
    print ("The yearly cashflow for this property is " + str(formattedYearCashFlow) + ".")
    print("Your first year's cash on cash return is "+ str(formattedCashOnCashReturn) + " percent.")
    
    
rentalCashFlow (184000, 25, 1300, 658.83, 105, 0, 65)


# In[ ]:




