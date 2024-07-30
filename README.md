# Image Handler Client

This module defines a schema for handling image information.

## Info

 - `filename` (str): The name of the image file.
 - `date` (str): The date associated with the image.
 - `theme` (str): The theme of the image.
 - `real` (bool): A boolean indicating whether the image is real or not.
 - `status` (Optional[ImageStatus]): The status of the image, defaulting to ImageStatus.UNVERIFIED.
   - Unverified
   - Verified
   - Rejected
