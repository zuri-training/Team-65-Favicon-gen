from django.db import models

class Images(models.Model):
  user_id = models.ForeignKey("User", on_delete=models.CASCADE)
  image_name = models.charfield(max_length=50)
  image_file_type = models.charfield(max_length=10, null=True)
  image_url = models.TextField()
  image_upload_date = models.DateField()

  def __str__(self):
    return self.user_id, self.image_name
      
class Favicon_Zip(models.Model):
  user_id = models.ForeignKey("User", on_delete=models.CASCADE)
  image_id = models.ForeignKey("Images", on_delete=models.CASCADE)
  favicon_name = models.charfield(max_length=50)
  favicon_zip_url = models.TextField()
  html_code = models.TextField()
  favicon_creation_date = models.DateField()
  
  def __str__(self):
    return self.user_id, self.favicon_name