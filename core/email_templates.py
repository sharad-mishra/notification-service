TEMPLATES = {
    "parcel_created": {
        "subject": "Your Parcel Has Been Created!",
        "body": (
            "Hello {user_name},\n\n"
            "Your parcel with Tracking ID {tracking_id} has been registered successfully.\n"
            "Pickup Address: {pickup_address}\n\n"
            "Thank you for using ParcelPro!"
        )
    },

    "parcel_in_transit": {
        "subject": "Your Parcel is On the Way!",
        "body": (
            "Hello {user_name},\n\n"
            "Your parcel with Tracking ID {tracking_id} is now in transit.\n"
            "Current Location: {current_location}\n\n"
            "You can track your parcel live using our app."
        )
    },

    "parcel_delivered": {
        "subject": "Your Parcel Has Been Delivered",
        "body": (
            "Hi {user_name},\n\n"
            "Your parcel with Tracking ID {tracking_id} has been delivered successfully.\n"
            "Delivered At: {delivery_time}\n\n"
            "We hope you had a great experience!\n"
            "Thank you for using ParcelPro!"
        )
    },

    "parcel_cancelled": {
        "subject": "Your Parcel Has Been Cancelled",
        "body": (
            "Hello {user_name},\n\n"
            "Your parcel with Tracking ID {tracking_id} has been cancelled.\n"
            "Reason: {cancellation_reason}\n\n"
            "If this was a mistake, please rebook using our app."
        )
    },

    "driver_assigned": {
        "subject": "Driver Assigned to Your Parcel",
        "body": (
            "Hi {user_name},\n\n"
            "A driver has been assigned to your parcel with Tracking ID {tracking_id}.\n"
            "Driver Name: {driver_name}\n"
            "Contact: {driver_contact}\n\n"
            "They will arrive shortly at your pickup address."
        )
    }
}
