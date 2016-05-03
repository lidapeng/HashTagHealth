package com.hashtag.yelpDataCollection;

public class Location {
	private String[] neighborhoods;
	private String cross_streets;

	private String state_code;

	private String[] display_address;

	private Coordinate coordinate;

	private String[] address;

	private String postal_code;

	private String geo_accuracy;

	private String country_code;

	private String city;

	public String[] getNeighborhoods() {
		return neighborhoods;
	}

	public void setNeighborhoods(String[] neighborhoods) {
		this.neighborhoods = neighborhoods;
	}

	public String getState_code() {
		return state_code;
	}

	public void setState_code(String state_code) {
		this.state_code = state_code;
	}

	public String[] getDisplay_address() {
		return display_address;
	}

	public void setDisplay_address(String[] display_address) {
		this.display_address = display_address;
	}

	public Coordinate getCoordinate() {
		return coordinate;
	}

	public void setCoordinate(Coordinate coordinate) {
		this.coordinate = coordinate;
	}

	public String[] getAddress() {
		return address;
	}

	public void setAddress(String[] address) {
		this.address = address;
	}

	public String getPostal_code() {
		return postal_code;
	}

	public void setPostal_code(String postal_code) {
		this.postal_code = postal_code;
	}

	public String getGeo_accuracy() {
		return geo_accuracy;
	}

	public void setGeo_accuracy(String geo_accuracy) {
		this.geo_accuracy = geo_accuracy;
	}

	public String getCountry_code() {
		return country_code;
	}

	public void setCountry_code(String country_code) {
		this.country_code = country_code;
	}

	public String getCity() {
		return city;
	}

	public void setCity(String city) {
		this.city = city;
	}

	@Override
	public String toString() {
		StringBuffer value = new StringBuffer("[");
		
		for(String val:address){
			value.append(val+",");
		}
		value.append("]");
		
		return coordinate.getLatitude() + "<>" + coordinate.getLongitude()
				+ "<>" + value.toString() + "<>" + city + "<>" + postal_code+"<>"+state_code;
	}

	public String getCross_streets() {
		return cross_streets;
	}

	public void setCross_streets(String cross_streets) {
		this.cross_streets = cross_streets;
	}
}