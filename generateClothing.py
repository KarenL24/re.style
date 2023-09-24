from serpapi import GoogleSearch
import json

image_urls = [
    "https://static.zara.net/photos///2023/I/0/1/p/8662/465/121/2/w/600/8662465121_2_1_1.jpg?ts=1694529483772" 
]


def main():
    google_reverse_image_data = {}

    for index, image_url in enumerate(image_urls, start=1):
        google_reverse_image_data[f"results for image {index}"] = {}

        params = {
            "api_key": "54e40b723baa78b2296f1c526992b0c8c8520f62ef594dff5660e9fe73c199e7",                
            "engine": "google_reverse_image",  
            "image_url": image_url,           
            "location": "Dallas",              
            "hl": "en",                        
            "gl": "us", 

            # other parameters
        }
        
        search = GoogleSearch(params)           # where data extraction happens on the SerpApi backend
        results = search.get_dict()     
        print(results)      

        # some queries may not include this information
        try:
            if results["knowledge_graph"]:
                knowledge_graph = {}
                
                knowledge_graph["title"] = results["knowledge_graph"]["title"]
                knowledge_graph["description"] = results["knowledge_graph"]["description"]
            
                google_reverse_image_data[f"results for image {index}"]["knowledge_graph"] = knowledge_graph
        except KeyError:
            print("keyerror")
        # some queries may not include organic results
        try:
            if results["image_results"]:
                google_reverse_image_data[f"results for image {index}"]["organic_results"] = []
            
            for result in results["image_results"]:
                image_results = {}
                
                image_results["position"] = result["position"]
                image_results["title"] = result["title"]
                image_results["link"] = result["link"]
                image_results["snippet"] = result["snippet"]
        
                google_reverse_image_data[f"results for image {index}"]["organic_results"].append(image_results)
        except KeyError:
            print("")
        # some queries may not include this information
        try:
            if results["inline_images"]:
                google_reverse_image_data[f"results for image {index}"]["inline_images"] = []
                
                for result in results["inline_images"]:
                    google_reverse_image_data[f"results for image {index}"]["inline_images"].append({
                        "source": result["source"],
                        "thumbnail": result["thumbnail"]
                    })
        except KeyError:
            print("inline erro")
    return google_reverse_image_data


if __name__ == "__main__":
    print(json.dumps(main(), indent=4, ensure_ascii=False))