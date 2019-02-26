using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace PostsRegisterer
{
    class Post
    {
        [JsonProperty("height")]
        public int Height { get; set; }
        [JsonProperty("width")]
        public int Width { get; set; }
        [JsonProperty("src")]
        public String Src { get; set; }
        [JsonProperty("id")]
        public String Id { get; set; }
    }
}
