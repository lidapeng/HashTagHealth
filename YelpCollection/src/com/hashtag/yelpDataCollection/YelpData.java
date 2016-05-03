package com.hashtag.yelpDataCollection;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

@JsonIgnoreProperties(ignoreUnknown = true)
public class YelpData
{
    private String rating_img_url_large;

    private String phone;

    private String snippet_text;

    private String rating_img_url;

    private Location location;

    private String review_count;

    private String is_closed;

    private String is_claimed;

    private String rating_img_url_small;

    private String url;

    private String id;

    private String image_url;

    private String name;
    private String menu_date_updated;
    private String menu_provider;
    private String distance;
    private String reservation_url;
    private String eat24_url;
    
    private String display_phone;

    private String snippet_image_url;

    private String mobile_url;

    private String[][] categories;

    private String rating;

    public String getRating_img_url_large ()
    {
        return rating_img_url_large;
    }

    public void setRating_img_url_large (String rating_img_url_large)
    {
        this.rating_img_url_large = rating_img_url_large;
    }

    public String getPhone ()
    {
        return phone;
    }

    public void setPhone (String phone)
    {
        this.phone = phone;
    }

    public String getSnippet_text ()
    {
        return snippet_text;
    }

    public void setSnippet_text (String snippet_text)
    {
        this.snippet_text = snippet_text;
    }

    public String getRating_img_url ()
    {
        return rating_img_url;
    }

    public void setRating_img_url (String rating_img_url)
    {
        this.rating_img_url = rating_img_url;
    }

    public Location getLocation ()
    {
        return location;
    }

    public void setLocation (Location location)
    {
        this.location = location;
    }

    public String getReview_count ()
    {
        return review_count;
    }

    public void setReview_count (String review_count)
    {
        this.review_count = review_count;
    }

    public String getIs_closed ()
    {
        return is_closed;
    }

    public void setIs_closed (String is_closed)
    {
        this.is_closed = is_closed;
    }

    public String getIs_claimed ()
    {
        return is_claimed;
    }

    public void setIs_claimed (String is_claimed)
    {
        this.is_claimed = is_claimed;
    }

    public String getRating_img_url_small ()
    {
        return rating_img_url_small;
    }

    public void setRating_img_url_small (String rating_img_url_small)
    {
        this.rating_img_url_small = rating_img_url_small;
    }

    public String getUrl ()
    {
        return url;
    }

    public void setUrl (String url)
    {
        this.url = url;
    }

    public String getId ()
    {
        return id;
    }

    public void setId (String id)
    {
        this.id = id;
    }

    public String getImage_url ()
    {
        return image_url;
    }

    public void setImage_url (String image_url)
    {
        this.image_url = image_url;
    }

    public String getName ()
    {
        return name;
    }

    public void setName (String name)
    {
        this.name = name;
    }

    public String getDisplay_phone ()
    {
        return display_phone;
    }

    public void setDisplay_phone (String display_phone)
    {
        this.display_phone = display_phone;
    }

    public String getSnippet_image_url ()
    {
        return snippet_image_url;
    }

    public void setSnippet_image_url (String snippet_image_url)
    {
        this.snippet_image_url = snippet_image_url;
    }

    public String getMobile_url ()
    {
        return mobile_url;
    }

    public void setMobile_url (String mobile_url)
    {
        this.mobile_url = mobile_url;
    }

    public String[][] getCategories ()
    {
        return categories;
    }

    public void setCategories (String[][] categories)
    {
        this.categories = categories;
    }

    public String getRating ()
    {
        return rating;
    }

    public void setRating (String rating)
    {
        this.rating = rating;
    }

    @Override
    public String toString()
    {
    	StringBuffer categoriesResult=new StringBuffer("");
       if(categories!=null){
    	   for(int i=0;i<categories.length;i++){
    		   categoriesResult.append("<>"+categories[i][0]);
    	   }
       }
    	
    	return name+"<>"+location.toString()+"<>"+phone+"<>"+rating+"<>"+review_count+categoriesResult;
    }

	public String getMenu_date_updated() {
		return menu_date_updated;
	}

	public void setMenu_date_updated(String menu_date_updated) {
		this.menu_date_updated = menu_date_updated;
	}

	public String getDistance() {
		return distance;
	}

	public void setDistance(String distance) {
		this.distance = distance;
	}

	public String getMenu_provider() {
		return menu_provider;
	}

	public void setMenu_provider(String menu_provider) {
		this.menu_provider = menu_provider;
	}

	public String getReservation_url() {
		return reservation_url;
	}

	public void setReservation_url(String reservation_url) {
		this.reservation_url = reservation_url;
	}

	public String getEat24_url() {
		return eat24_url;
	}

	public void setEat24_url(String eat24_url) {
		this.eat24_url = eat24_url;
	}
}
