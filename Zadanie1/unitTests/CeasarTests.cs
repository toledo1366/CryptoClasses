using Ceasar.Services;
using NUnit.Framework;
using System;
using System.Collections.Generic;
using System.Text;

namespace unitTests
{
    public class CeasarTests
    {
        [Test]
        public void Decrypt_GivenString_WhenCalled()
        {
            string text = "abcde";
            var ceasar = new CeasarDecryptor();
            var result = ceasar.Decryptor(text, 3);
            Assert.AreEqual("defgh", result);
        }
    }
}
