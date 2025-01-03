from django.shortcuts import render, redirect
from hotelapp.models import *
from userapp.models import *
from .models import *

def addBooking(request, id):
    if request.method == 'POST':
        # Retrieve the category instance
        cat_data = Category.objects.get(id=id)
        
        # Retrieve the user instance (assuming the user is logged in)
        email="a@gmail.com"
        user = User.objects.get(email=email)  # Adjust this based on your authentication logic
        
        # Retrieve form data
        no_of_rooms = request.POST['no_of_rooms']
        no_of_people = request.POST['no_of_people']
        check_in = request.POST['check_in']
        check_out = request.POST['check_out']
        total_price = float(no_of_rooms) * cat_data.price_per_room
        
        # Create and save the booking instance
        booking = Booking(
            user=user,
            hotel=cat_data.hotel,
            room_category=cat_data,
            no_of_rooms=no_of_rooms,
            no_of_people=no_of_people,
            check_in=check_in,
            check_out=check_out,
            total_price=total_price
        )
        booking.save()
        
        return redirect('bookinglist')  # Redirect to the booking list page after successful booking
    else:
        cat_data = Category.objects.get(id=id)
        return render(request, 'bookingapp/AddBooking.html', {'cat_data': cat_data})

def bookingList(request):
    # Retrieve all bookings for the logged-in user
    email="a@gmail.com"
    user = User.objects.get(email=email)  # Adjust this based on your authentication logic
    bookings = Booking.objects.filter(user=user)
    return render(request, 'bookingapp/BookingList.html', {'bookings': bookings})

def deleteBooking(request, id):
    # Retrieve the booking instance by ID
    booking = Booking.objects.get(id=id)
    
    if request.method == 'POST':
        # Delete the booking
        booking.delete()
        return redirect('bookinglist')  # Redirect to the booking list after deletion
    
    # Render a confirmation template (optional)
    return render(request, 'bookingapp/confirm_delete_booking.html', {'booking': booking})