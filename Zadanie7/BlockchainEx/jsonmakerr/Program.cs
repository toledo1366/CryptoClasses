using Newtonsoft.Json;
using System;

namespace jsonmakerr
{
    class Program
    {
        static void Main(string[] args)
        {
            Data d1 = new Data { Sender = "Henry", Receiver = "MaHesh", Amount = 10 };
            Data d2 = new Data { Sender = "MaHesh", Receiver = "Henry", Amount = 5 };
            Data d3 = new Data { Sender = "MaHesh", Receiver = "Henry", Amount = 5 };

            Blockchain phillyCoin = new Blockchain();
            phillyCoin.AddBlock(new Block(DateTime.Now, null, d1));
            phillyCoin.AddBlock(new Block(DateTime.Now, null, d2));
            phillyCoin.AddBlock(new Block(DateTime.Now, null, d3));

            Console.WriteLine(JsonConvert.SerializeObject(phillyCoin, Formatting.Indented));
            Console.ReadKey();
        }
    }
}
