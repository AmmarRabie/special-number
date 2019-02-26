using System;
using Newtonsoft.Json;

namespace PostsRegisterer
{
    class PostInfo
    {
        public PostInfo(String phone, String price, String message)
        {
            this.Phone = phone;
            this.Price = price;
            this.Message = message;
        }

        [JsonProperty("phone")]
        public String Phone { get; set; }
        [JsonProperty("price")]
        public String Price { get; set; }

        [JsonProperty("message")]
        public String Message { get; set; }
    }
}
