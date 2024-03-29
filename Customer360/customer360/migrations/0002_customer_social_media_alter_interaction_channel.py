# Generated by Django 4.2.5 on 2023-09-08 22:43

from django.db import migrations, models


class Migration(migrations.Migration):
    """
    This is a Django migration file that adds a new field and alters an existing field in the database schema.
    It builds upon the previous migration ('0001_initial').

    Dependencies:
    This migration depends on the previous migration ('0001_initial') which created the Customer and Interaction models.

    Operations:
    - AddField: Adds a new field 'social_media' to the 'Customer' model.
      The 'social_media' field is a CharField allowing blank values with a maximum length of 100.
      This field will store the customer's social media information, such as usernames or handles.

    - AlterField: Modifies the 'channel' field in the 'Interaction' model.
      The 'channel' field now includes a new choice 'social_media' in addition to 'phone', 'sms', 'email', and 'letter'.
      This change allows interactions to be categorized under the 'Social Media' channel as well.

    Note:
    - This migration extends the existing database schema by adding a new field to the 'Customer' model
      and updating the 'Interaction' model to include a new channel option for social media interactions.
    - 'social_media' field in 'Customer' model allows storing social media information.
    - 'channel' field in 'Interaction' model now includes 'social_media' as a communication channel option.
    - This update enhances the flexibility of the database schema to accommodate social media interactions.
    """
    dependencies = [
        ('customer360', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='social_media',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='interaction',
            name='channel',
            field=models.CharField(choices=[
                ('phone', 'Phone'),
                ('sms', 'SMS'),
                ('email', 'Email'),
                ('letter', 'Letter'),
                ('social_media', 'Social Media')
            ], max_length=15),
        ),
    ]
