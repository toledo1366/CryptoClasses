using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp2
{
    class Blockchain
    {
        public IList<Block> Chain = new List<Block>();

        public Blockchain()
        {
            AddGenesisBlock();
        }

        public Block CreateGenesisBlock()
        {
            return new Block(DateTime.Now, null, null);
        }

        public void AddGenesisBlock()
        {
            Chain.Add(CreateGenesisBlock());
        }

        public void AddBlock(Block block)
        {
            Block latestBlock = Chain[Chain.Count - 1];
            block.Index = latestBlock.Index + 1;
            block.PreviousHash = latestBlock.Hash;
            block.Hash = block.CalculateHash();
            Chain.Add(block);
        }
    }
}
