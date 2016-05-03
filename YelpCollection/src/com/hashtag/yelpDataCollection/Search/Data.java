package com.hashtag.yelpDataCollection.Search;

import java.io.*;
import java.util.List;
import java.util.concurrent.TimeUnit;

import com.fasterxml.jackson.core.JsonGenerationException;
import com.fasterxml.jackson.core.JsonParseException;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.JsonMappingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.hashtag.yelpDataCollection.Search.YelpAPI.YelpAPICLI;
import com.hashtag.yelpDataCollection.YelpData;
public class Data {

	BufferedWriter bw;
	YelpAPI yelpApi;
	public void readFile(String filename, String FilePath) throws IOException {

		BufferedReader br = new BufferedReader(new FileReader(filename));
		bw = new BufferedWriter(new FileWriter(FilePath));
		String str = null;
		int j = 0;
		int exceptionCount=0;
		yelpApi = new YelpAPI("CONSUMER_KEY ",
				"CONSUMER_SECRET ",
				"TOKEN",
				"TOKEN_SECRET ");
		while ((str = br.readLine()) != null) {

			if (j ==24000) {
				break;
			}
			try{
				startCollection(str);
				j++;
			}catch(Exception e){
				exceptionCount++;
			}
			
			
			System.out.println(j);
		}
		System.out.println("exception count for file->"+filename+" "+exceptionCount);
		System.out.println(j);
	}

	public void startCollection(String location) {

		YelpAPICLI yelpApiCli = new YelpAPICLI();
		try {

			// new JCommander(yelpApiCli, args);
			String split[] = location.split(",");
			yelpApiCli.location = split[1].trim() + "," + split[0].trim();
			yelpApiCli.RadiusFilter = "1000";
			
			String value = YelpAPI.queryAPI(yelpApi, yelpApiCli);
			if(value.contains("error")){
				return;
			}
			String val = value.substring(value.indexOf("\"businesses\":")
					+ "\"businesses\":".length());
			ObjectMapper mapper = new ObjectMapper();
			List<YelpData> obj = mapper.readValue(val,
					new TypeReference<List<YelpData>>() {
					});
			

			for (YelpData yelpData : obj) {
				bw.write(yelpData.toString());
				bw.newLine();
			}

		} catch (JsonGenerationException e) {
			e.printStackTrace();
		} catch (JsonMappingException e) {
			e.printStackTrace();
		} catch (JsonParseException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}
	
	public void close(){
		try {
			bw.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	public static void main(String args[]) throws IOException {
		Data obj = new Data();
		//String folder = "E:\\yelpCollection\\yelpCoordinate\\pts0.02_new.txt";
		String FileWrite=args[0];
		File folder=new File(args[1]);
		File[] files= folder.listFiles();
		for(File file:files){
			obj.readFile(file.getAbsolutePath(),FileWrite+File.separator+file.getName());
			obj.close();
			System.out.println(file.getName()+" is done");
			 try {
				System.out.println("sleeping");
				TimeUnit.HOURS.sleep(22);
				System.out.println("wokeup");
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
		}
		
	}
}