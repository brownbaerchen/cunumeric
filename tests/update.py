# Copyright 2021 NVIDIA Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import legate.numpy as lg


def test():
    C = lg.random.randn(2, 3, 5)
    IFOGf = lg.random.randn(2, 3, 20)
    C[1] = 1.0
    C[1] += IFOGf[1, :, :5] * IFOGf[1, :, 15:]
    temp = IFOGf[1, :, :5] * IFOGf[1, :, 15:]
    assert not lg.array_equal(C[1], temp)

    print(C[1])
    print(temp)
    return


if __name__ == "__main__":
    test()