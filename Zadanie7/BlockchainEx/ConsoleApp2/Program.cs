using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp2
{
    class Program
    {
        static void Main(string[] args)
        {
            Data d1 = new Data { Sender = "Henry", Receiver = "MaHesh", Amount = 10f };
            Data d2 = new Data { Sender = "MaHesh", Receiver = "Henry", Amount = 5f };
            Data d3 = new Data { Sender = "MaHesh", Receiver = "Henry", Amount = 5f };
            Blockchain phillyCoin = new Blockchain();
            phillyCoin.AddBlock(new Block(DateTime.Now, null, d1));
            phillyCoin.AddBlock(new Block(DateTime.Now, null, d2));
            phillyCoin.AddBlock(new Block(DateTime.Now, null, d3));

            Console.WriteLine(JsonConvert.SerializeObject(phillyCoin, Formatting.Indented));
            Console.ReadKey();
        }
    }
}
