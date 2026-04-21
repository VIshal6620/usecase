from django.db import models

class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    loginId = models.EmailField()
    password = models.CharField(max_length=20)
    confirmPassword = models.CharField(max_length=20)
    dob = models.DateField(max_length=20)
    address = models.CharField(max_length=50, default='')
    gender = models.CharField(max_length=30, default='')
    mobileNumber = models.CharField(max_length=30, default='')
    roleId = models.IntegerField()
    roleName = models.CharField(max_length=50)


    def to_json(self):
        data = {
            'id': self.id,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'loginId': self.loginId,
            'password': self.password,
            'confirmPassword': self.confirmPassword,
            'dob': self.dob.strftime('%Y-%m-%d'),
            'address': self.address,
            'gender': self.gender,
            'mobileNumber': self.mobileNumber,
            'roleId': self.roleId,
            'roleName': self.roleName
        }
        return data

    class Meta:
        db_table = 'sos_user'

class Role(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)


    def to_json(self):
        data ={
            'id': self.id,
            'name': self.name,
            'description': self.description
        }
        return data

    class Meta:
        db_table = 'sos_role'


class Loan(models.Model):
    loanAmount = models.CharField(max_length=50)
    interestRate = models.CharField(max_length=50)
    issueDate = models.DateField(max_length=20)

    def to_json(self):
        data = {
            'id': self.id,
            'loanAmount': self.loanAmount,
            'interestRate': self.interestRate,
            'issueDate': self.issueDate
        }

        return data

    class Meta:
        db_table = 'sos_loan'


class Gym(models.Model):
    memberName = models.CharField(max_length=50)
    membershipType = models.CharField(max_length=30)
    startDate = models.DateField(max_length=20)
    endDate = models.DateField(max_length=20)

    def to_json(self):
        data = {
            'id': self.id,
            'memberName': self.memberName,
            'membershipType': self.membershipType,
            'startDate': self.startDate,
            'endDate': self.endDate,
        }
        return data

    class Meta:
        db_table = 'sos_gym'

class Travel(models.Model):
    travelerName = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    startDate = models.DateField(max_length=20)
    endDate = models.DateTimeField(max_length=20)

    def to_json(self):
        data = {
            'id': self.id,
            'travelerName': self.travelerName,
            'destination': self.destination,
            'startDate': self.startDate,
            'endDate': self.endDate,
        }
        return data

    class Meta:
        db_table = 'sos_travel'


class Holiday(models.Model):
    holidayCode = models.CharField(max_length=20)
    holidayName = models.CharField(max_length=50)
    holidayDate = models.DateField(max_length=20)
    holidayType = models.CharField(max_length=50)

    def to_json(self):
        data = {
            'id': self.id,
            'holidayCode': self.holidayCode,
            'holidayName': self.holidayName,
            'holidayDate': self.holidayDate,
            'holidayType': self.holidayType,
        }
        return data

    class Meta:
     db_table = 'sos_holiday'

class Speaker(models.Model):
    speakerName = models.CharField(max_length=50)
    topic = models.CharField(max_length=60)
    organization = models.CharField(max_length=50)

    def to_json(self):
        data= {
            'id': self.id,
            'speakerName': self.speakerName,
            'topic': self.topic,
            'organization': self.organization
        }

        return data

    class Meta:
        db_table = 'sos_speaker'

class PlantNursery(models.Model):
    plantName = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    quantity = models.CharField(max_length=30)

    def to_json(self):
        data = {
            'id': self.id,
            'plantName': self.plantName,
            'category': self.category,
            'quantity': self.quantity
        }

        return data

    class Meta:
        db_table = 'sos_plant_nursery'


class Event(models.Model):
    participantName = models.CharField(max_length=50)
    eventName = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    registrationDate = models.DateField(max_length=15)

    def to_json(self):
        data ={
            'id': self.id,
            'participantName': self.participantName,
            'eventNAme': self.eventName,
            'email': self.email,
            'registrationDate': self.registrationDate
        }

        return data

    class Meta:
        db_table = 'sos_event'


class Reward(models.Model):
    rewardCode = models.CharField(max_length=50)
    rewardName = models.CharField(max_length=50)
    rewardAmount = models.CharField(max_length=50)
    rewardStatus = models.CharField(max_length=50)

    def to_json(self):
        data = {
            'id': self.id,
            'rewardCode': self.rewardCode,
            'rewardName': self.rewardName,
            'rewardAmount': self.rewardAmount,
            'rewardStatus': self.rewardStatus
        }

        return data

    class Meta: db_table = 'sos_reward'

class Rejection(models.Model):
    rejectionCode = models.CharField(max_length=50)
    requestName = models.CharField(max_length=50)
    rejectionReason = models.CharField(max_length=50)
    rejectionStatus = models.CharField(max_length=50)

    def to_json(self):
        data = {
            'id': self.id,
            'rejectionCode': self.rejectionCode,
            'requestName': self.requestName,
            'rejectionReason': self.rejectionReason,
            'rejectionStatus': self.rejectionStatus
        }

        return data

    class Meta: db_table = 'sos_rejection'

class BloodDonation(models.Model):
    donorName = models.CharField(max_length=50)
    bloodGroup = models.CharField(max_length=10)
    donationDate = models.DateField(max_length=15)
    contactNumber = models.CharField(max_length=15)

    def to_json(self):
        data = {
            'id': self.id,
            'donorName': self.donorName,
            'bloodGroup': self.bloodGroup,
            'donationDate': self.donationDate,
            'contactNumber': self.contactNumber
        }

        return data

    class Meta: db_table = 'sos_blood_donation'

class Security(models.Model):
    StaffName = models.CharField(max_length=50)
    shift = models.CharField(max_length=30)
    salary = models.CharField(max_length=30)

    def to_json(self):
        data = {
            'id': self.id,
            'StaffName': self.StaffName,
            'shift': self.shift
        }

        return data

    class Meta: db_table = 'sos_security'


class NotificationTemplate(models.Model):
    templateCode = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=60)
    status = models.CharField(max_length=50)

    def to_json(self):
        data = {
            'id': self.id,
            'templateCode': self.templateCode,
            'title': self.title,
            'content': self.content,
            'status': self.status
        }

        return data

    class Meta: db_table = 'sos_notification_template'


class Limit(models.Model):
    limitCode = models.CharField(max_length=50)
    limitName = models.CharField(max_length=30)
    maxValue = models.CharField(max_length=30)
    status = models.CharField(max_length=50)

    def to_json(self):
        data = {
            'id': self.id,
            'limitCode': self.limitCode,
            'limitName': self.limitName,
            'maxValue': self.maxValue,
            'status': self.status
        }

        return data

    class Meta:
        db_table = 'sos_limit'


class Purge(models.Model):
    purgeCode = models.CharField(max_length=30)
    dataType = models.CharField(max_length=30)
    lastRunDate = models.DateField(max_length=20)
    status = models.CharField(max_length=60)

    def to_json(self):
        data = {
            'id': self.id,
            'purgeCode': self.purgeCode,
            'dataType': self.dataType,
            'lastRunDate': self.lastRunDate,
            'status': self.status
        }

        return data

    class Meta:
        db_table = 'sos_purge'