from django.shortcuts import render,redirect
from .models import*

def transaction_details(request):
	transaction = transactionDetail.objects.all()
	return render(request, 'bankapp/transaction.html',{'transaction':transaction})



def home(request):
	return render(request, 'bankapp/home.html',{})


def customer_details(request):
	customer = customerDetail.objects.all()
	if request.method == "POST":
		email = request.POST.get('email')
		semail = request.POST.get('semail')
		amt = request.POST.get('amt')
		try:
			amt = int(amt)
		except:
			print("enter amount")
		for i in customer:
			print(email)
			if i.email == email:
				j = i
				id = i.id
				break
		for i in customer:
			print(i.email,i.available_bal,semail)
			if i.email==semail and amt< i.available_bal and amt>0 :
				available_bal = i.available_bal - amt
				available_bal2 = j.available_bal + amt
				try:
					query1 = transactionDetail(name=i.name, email=i.email,
	                                            debitted_amt=amt ,credited_amt=0 , account_bal=available_bal)

					query2 = customerDetail(id=i.id, available_bal=available_bal, email=i.email
	                                                , name=i.name)
					query3 = transactionDetail(name=j.name, email=j.email,
	                                            debitted_amt=0 ,credited_amt=amt , account_bal=available_bal2)
					query4 = customerDetail(id=id, available_bal=available_bal2, email=j.email
	                                                , name=j.name)
					query2.save()
					query1.save()
					query4.save()
					query3.save()
	                
					return redirect('/customer')


					break
				except:
					print("transaction failed")
					break
			else:
				print("invalid data")
	return render(request, 'bankapp/customer.html',{'customer':customer})	

