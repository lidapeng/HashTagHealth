package com.hashtag.yelpDataCollection;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.List;

import com.fasterxml.jackson.core.JsonGenerationException;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.core.util.BufferRecycler;
import com.fasterxml.jackson.databind.JsonMappingException;
import com.fasterxml.jackson.databind.ObjectMapper;

public class DataCollection {

	
	public static void main(String args[]){
		ObjectMapper mapper = new ObjectMapper();
		
		try {
			// Convert object to JSON string and save into a file directly
			//YelpData obj=new YelpData();
			String str=null;
	StringBuffer buf=new StringBuffer();
			BufferedReader br=new BufferedReader(new FileReader("/Users/surajkath/Documents/sampleYelp.json"));
			while((str=br.readLine())!=null){
				buf.append(str);
			}
			
			List<YelpData>obj=mapper.readValue(buf.toString(), new TypeReference<List<YelpData>>(){});
			

			// Convert object to JSON string
			String jsonInString = mapper.writeValueAsString(obj);
			System.out.println(jsonInString);

			// Convert object to JSON string and pretty print
			

		} catch (JsonGenerationException e) {
			e.printStackTrace();
		} catch (JsonMappingException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}
